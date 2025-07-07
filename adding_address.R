# Importing libraries
library(tidyverse)
library(janitor)

# Creating a cleaning function to clean agency names
clean_agency <- function(df) {
  df %>%
    str_to_lower() %>%
    str_replace_all("\\.", "") %>%       
    str_replace_all("'s\\b", "") %>% 
    str_replace_all("’s\\b", "") %>% 
    str_replace_all(regex("\\bcity of\\b", ignore_case = TRUE), "") %>%
    str_replace_all(regex("\\b(department|dept|office|bureau|division|unit)\\b", ignore_case = TRUE), "") %>%
    str_replace_all(regex("\\bsaint\\b", ignore_case = TRUE), "st") %>%
    str_squish() %>%
    trimws()
}

# Loading agency data. This data is downloaded here: https://www.icpsr.umich.edu/web/NACJD/studies/38771/summary
lookup <- da38771.0001 %>%
  clean_names() %>%
  mutate(
    agency = clean_agency(agencyname),
    state = str_to_upper(recode(state, !!!state_names)),
    
    # Dooing agency-specific cleaning
    agency = case_when(
      agency == "virginia state police" & state == "VIRGINIA" ~ "virginia of state police",
      agency == "vera beach police" & state == "FLORIDA" ~ "vero beach police",
      agency == "sewalls point police" & state == "FLORIDA" ~ "sewall point police",
      agency == "sarasota-manatee airport authority police" & state == "FLORIDA" ~ "sarasota manatee airport authority police",
      agency == "pittsburg police" & state == "NEW HAMPSHIRE" ~ "pittsburgh police",
      agency == "lake clarke shores police" & state == "FLORIDA" ~ "lake clark shores police",
      agency == "indian river shores public safety" & state == "FLORIDA" ~ "indian river shores of public safety",
      agency == "indialantic police" & state == "FLORIDA" ~ "indiatlantic police",
      agency == "franklin county sheriff" & state == "PENNSYLVANIA" ~ "franklin county sheriffs",
      agency == "fort myers police" & state == "FLORIDA" ~ "ft myers police",
      agency == "daytona beach shores of public safety" & state == "FLORIDA" ~ "daytona beach shores public safety",
      agency == "berrien county sheriff" & state == "MICHIGAN" ~ "berrian county sheriff",
      agency == "neptune beach public safety" & state == "FLORIDA" ~ "neptune beach police",
      agency == "alachua police" & state == "FLORIDA" ~ "alachua police departent",
      agency == "virginia marine resources commission police" & state == "VIRGINIA" ~ "virginia marine resources commission",
      agency == "las vegas metro police" & state == "NEVADA" ~ "las vegas metropolitan police",
      agency == "florida of corrections - of the inspector general" & state == "FLORIDA" ~ "florida of corrections",
      agency == "florida of agriculture and consumer services - of agricultural law enforcement" & state == "FLORIDA" ~ "florida of agriculture",
      agency == "florida of financial services - of insurance fraud" & state == "FLORIDA" ~ "florida of financial services",
      agency == "montana of justice - of criminal investigation" & state == "MONTANA" ~ "montana of justice",
      agency == "florida fish & wildlife conservation commission - of law enforcement" & state == "FLORIDA" ~ "florida fish and wildlife conservation commission",
      agency == "florida fish & wildlife conservation commission - of law enforcement" & state == "FLORIDA" ~ "florida fish and wildlife conservation commission",
      agency == "indiatlantic police" & state == "FLORIDA" ~ "indialantic police",
      agency == "orange county sheriff" & state == "FLORIDA" ~ "orange county corrections",
      agency == "osceola county sheriff" & state == "FLORIDA" ~ "osceola county corrections",
      agency == "university of central florida police" & state == "FLORIDA" ~ "university of central florida board of trustees",
      agency == "university of west florida police" & state == "FLORIDA" ~ "university of west florida board of trustees",
      agency == "volusia county of public protection" & state == "FLORIDA" ~ "volusia county of corrections",
      agency == "bullitt county sheriff" & state == "KENTUCKY" ~ "bullitt county detention center",
      agency == "grayson county sheriff" & state == "KENTUCKY" ~ "grayson county detention center",
      agency == "oldham county police" & state == "KENTUCKY" ~ "oldham county detention center",
      agency == "berrian county sheriff" & state == "MICHIGAN" ~ "berrian county sheriff offic",
      agency == "louisiana state police" & state == "LOUISIANA" ~ "louisiana state patrol",
      agency == "louisiana of alcohol and tobacco control enforcement" & state == "LOUISIANA" ~ "louisiana alcohol and tobacco control",
      agency == "florida southwestern state college of public safety" & state == "FLORIDA" ~ "florida southwestern state college police",
      TRUE ~ agency),
    
    # Cleaning variables
    agencyid = trimws(agencyid),
    ori9 = trimws(ori9),
    zip = trimws(zip),
  ) %>%
  select(state, agency, population, zip, agencyid, ori9, opbudget, agencysamptype) %>%
  distinct()

# Creating a joined dataframe
joined_df <- participating_data %>%
  mutate(
    agency = clean_agency(law_enforcement_agency)
  ) %>%
  left_join(lookup, by = c("state", "agency")) %>%
  select(date,
         state, 
         county,
         zip, 
         agency, 
         agency_id = agencyid,
         ori = ori9, 
         type = support_type, 
         population_policed = population, 
         operating_budget = opbudget,
         agency_type = agencysamptype)