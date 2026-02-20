read_excel("participatingAgencies01262026pm.xlsx") %>%
  clean_names() %>%
  mutate(
    agency = str_to_lower(law_enforcement_agency) %>%
      str_replace_all("’", "'") %>%
      str_squish(),
    classification = case_when(
      str_detect(agency, "university|college") ~ "University Police",
      str_detect(agency, "airport") ~ "Airport Police",
      str_detect(agency, "drug|alcohol|narcotics") ~ "Drug / Alcohol Police",
      str_detect(agency, "lottery|gambling|gaming") ~ "Lottery",
      str_detect(agency, "sheriff") ~ "Sheriff",
      str_detect(agency, "state police|state patrol") ~ "State Police",
      str_detect(agency, "highway") ~ "Highway Police",
      str_detect(agency, "police department|police departement") ~ "Local Police Department",
      str_detect(agency, "correction|jail|prison|detention") ~ "Corrections/Jail",
      str_detect(agency, "constable") ~ "Constable",
      str_detect(agency, "marshal") ~ "Marshal",
      str_detect(agency, "national guard") ~ "National Gaurd",
      str_detect(agency, "state guard") ~ "State Gaurd",
      str_detect(agency, "district attorney") ~ "District Attorney",
      str_detect(agency, "department of public safety") ~ "Department of Public Safety",
      str_detect(agency, "wildlife") ~ "Wildlife",
      str_detect(agency, "attorney general") ~ "Attorney General",
      str_detect(agency, "military") ~ "Military",
      str_detect(agency, "homeland security") ~ "Homeland Security",
      TRUE ~ "Other Agency"
    )
  ) %>%
  tabyl(classification) %>%
  arrange(-n)
