# Loading libraries
library(tidyverse)
library(readxl)
library(janitor)
library(fuzzyjoin)
library(stringdist)
library(tidycensus)

# Loading decennial data
pop_2020 <- get_decennial(
  geography = "county",
  variables = "P1_001N",
  year = 2020,
  sumfile = "pl",
) %>%
  clean_names() %>%
  rename(
    county = name,
    population_2020 = value
  ) %>%
  select(county, population_2020)

# Loading ACS 2023 data
pop_acs_2023 <- get_acs(
  geography = "county",
  variables = "B01003_001",
  year = 2023,
  survey = "acs5",
) %>%
  clean_names() %>%
  rename(
    county = name,
    population_acs_2023 = estimate,
  ) %>%
  select(county, population_acs_2023)

# Merging population data frames + cleaning
population <- pop_2020 %>%
  full_join(pop_acs_2023, by = "county") %>%
  separate(county, into = c("county", "state"), sep = ",\\s*", remove = TRUE) %>%
  mutate(
    state  = str_to_lower(state) %>% str_squish(),
    county = str_to_lower(county) %>%
      str_remove_all("\\.") %>%
      str_remove_all("county") %>%
      str_squish()
  )

# Loading 287g agencies
data <- read_excel("participatingAgencies01262026pm.xlsx") %>%
  clean_names() %>%
  
  # Cleaning variables
  mutate(
    state = str_to_lower(state) %>% str_squish(),
    county = str_to_lower(county) %>%
      str_remove_all("\\.") %>%
      str_remove_all("county") %>%
      str_squish(),
    agency = str_to_lower(law_enforcement_agency) %>%
      str_replace_all("’", "'") %>%
      str_remove_all("\\b(office|department)\\b") %>%
      str_squish(),
    
    # Renaming counties
    county = case_when(
      
      # AL
      state == "alabama" & county == "frankin" ~ "franklin",
      state == "arkansas" & county == "pulaksi" ~ "pulaski",
      state == "arkansas" & county == "pop" ~ "pope",
      
      # FL
      state == "florida" & county == "flager" ~ "flagler",
      state == "florida" & county == "lake conty" ~ "lake",
      state == "florida" & county == "st luice" ~ "st lucie",
      
      # IA
      state == "indiana" & county == "stueben" ~ "steuben",
      
      # LA
      state == "louisiana" & county == "saint landry" ~ "st landry parish",
      state == "louisiana" & county == "calacasieu parish" ~ "calcasieu parish",
      state == "louisiana" & county == "arcadia" ~ "arcadia",
      state == "louisiana" & county == "german coast" ~ "st charles parish",
      
      # MI
      state == "michigan" & county == "berrian" ~ "berrien",
      
      # NC
      state == "north carolina" & county == "albem" ~ "albemarle",
      
      # PA
      state == "pennsylvania" & county == "miffin" ~ "mifflin",
      state == "pennsylvania" & county == "alleghany" ~ "allegheny",
      
      # TX
      state == "texas" & county == "fall" ~ "falls",
      state == "texas" & county == "guadalupe conty" ~ "guadalupe",
      
      # VA
      state == "virginia" & county == "hopewell" ~ "hopewell city",
      
      TRUE ~ county
    )
  ) %>%
  
  # Keeping distinct state, county, agency pairs
  distinct(state, county, agency)

# Joining population with 287g agreement
joined <- data %>%
  left_join(population, by = c("state", "county"))

# Filtering the "joined" to just Sheriffs
sheriff <- joined %>%
  filter(str_detect(agency, "sheriff"))

# Summary by state
state_summary <- sheriff %>%
  group_by(state) %>%
  summarize(
    agency_count = n_distinct(agency),
    population_count_2020 = sum(population_2020, na.rm = TRUE),
    population_count_2023 = sum(population_acs_2023, na.rm = TRUE)
  ) %>%
  ungroup() %>%
  adorn_totals()

# State breakdown
state_summary
