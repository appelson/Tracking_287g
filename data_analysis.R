# --------------------- Reading in Data ------------------------
# Loading Libraries
library(dplyr)
library(purrr)
library(stringr)
library(janitor)
library(readxl)
library(ggplot2)
library(showtext)
library(lubridate)

# Loading data
parent_folder <- "sheets"

# Defining the data folders
folders <- list.dirs(parent_folder, full.names = FALSE, recursive = FALSE) %>%
  keep(~ str_detect(.x, "sheets_"))

# Getting excel files and making them unique
extract_excel_files <- function(folder) {
  list.files(file.path(parent_folder, folder), pattern = "\\.xlsx$", full.names = TRUE)
}

all_files <- folders %>%
  map(extract_excel_files) %>%
  unlist() %>%
  unique()

unique_files <- all_files[match(unique(basename(all_files)), basename(all_files))]

# Defining the participating and pending files
participating_files <- unique_files %>% str_subset("participating")
pending_files <- unique_files %>% str_subset("pending")

# Extracting data
read_and_tag_date <- function(file_paths) {
  map_df(file_paths, function(path) {
    filename <- basename(path)
    datetime_str <- str_extract(filename, "[0-9]{8}(am|pm)")
    date_str <- str_sub(datetime_str, 1, 8)
    am_pm <- str_sub(datetime_str, 9, 10)
    date_parsed <- mdy(date_str)
    datetime_tag <- paste(date_parsed, am_pm)
    
    read_excel(path) %>%
      mutate(date = datetime_tag)
  }) %>%
    clean_names()
}

participating_data <- read_and_tag_date(participating_files)
pending_data <- read_and_tag_date(pending_files)

# --------------------- Analyzing Data ------------------------

summary_df <- participating_data %>%
  group_by(state) %>%
  summarise(
    base = sum(date == "2025-05-16 am"),
    new = sum(date == max(date)),
    diff = new - base,
    .groups = "drop"
  ) %>%
  arrange(diff) %>%
  mutate(
    state = str_to_title(state),
    state = factor(state, levels = state)
  )

font_add_google("Roboto Condensed", "roboto_condensed")
showtext_auto()

latest_date <- max(as.Date(str_remove(participating_data$date, "am|pm")))
latest_date_label <- format(latest_date, "%B %d, %Y")
agency_label <- "Participating Agencies"

# Creating a plot of increases
increase_plot <- summary_df %>%
  filter(diff != 0) %>%
  ggplot(aes(x = state, y = diff)) +
  geom_segment(aes(x = state, xend = state, y = 0, yend = diff), color = "grey70") +
  geom_point(color = "#1976D2", size = 4, alpha = 0.7) +
  coord_flip() +
  theme_minimal(base_size = 14, base_family = "roboto_condensed") +
  labs(
    title = str_to_upper(paste("Increase in", agency_label, "with 287(g) Agreements")),
    subtitle = paste0("Difference between May 16, 2025 and the latest date, ", latest_date_label),
    x = NULL,
    y = paste("Additional", agency_label)
  ) +
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    text = element_text(face = "bold"),
    plot.subtitle = element_text(face = "plain")
  )

# Creating a plot of top 20 agencies
top20_plot <- summary_df %>%
  arrange(new) %>%
  tail(20) %>%
  mutate(state = factor(state, levels = state)) %>%
  ggplot(aes(x = state, y = new)) +
  geom_col(fill = "#1976D2", alpha = 0.7) +
  coord_flip() +
  theme_minimal(base_size = 14, base_family = "roboto_condensed") +
  labs(
    title = str_to_upper(paste("Number of", agency_label, "with 287(g) Agreements")),
    subtitle = paste0("Top 20, as of the latest date, ", latest_date_label),
    x = NULL,
    y = agency_label
  ) +
  theme(
    panel.grid.major.y = element_blank(),
    panel.grid.minor = element_blank(),
    text = element_text(face = "bold"),
    plot.subtitle = element_text(face = "plain")
  )

# Saving plots
png(filename = "plots/add_agreements.png", 
    width = 2900,
    height = 2000,
    res = 300)
print(increase_plot)
dev.off()

png(filename = "plots/n_agreements.png", 
    width = 2900,
    height = 2000,
    res = 300)
print(top20_plot)
dev.off()
