# Tracking 287(g)

This repository downloads data and agreements from the **287(g)** program and organizes them to be used by journalists, advocates, and the public. The scraper runs daily, extracting data from the official [ICE 287(g) page](https://www.ice.gov/identify-and-arrest/287g). 

**The data is saved in three main folders:**

- **`agreements/`**: Contains PDFs of all 287(g) agreements between law enforcement agencies and ICE, categorized by download date/time, state, and agency.
- **`sheets/`**: Stores Excel files listing participating and pending agencies, as published on the ICE website, categorized by download date/time.
- **`archive/`**: Contains 287(g) sheets and agreements backfilled from the [Wayback Machine](http://web.archive.org/) between January 2021 and when this scraper was created. This is meant to fill in *some* of the missing data for the years before this project. It is split into `before_2025/` (when ICE published data as an HTML table) and `after_2025/` (when ICE switched to downloadable `.xlsx` sheets), plus the `raw/` HTML captures used to build both. The folder `before_2025/` contains only the sheets that differ from the one before them, so the data is shown in full but without consecutive duplicates.

### *Note*
This project was created in my personal capacity. Should you have any questions or suggestions for other public immigration data you would like to see tracked, you can contact me at **elijahappelson@gmail.com**.

## Updates
- **June 8th, 2026:** Included archived data, downloaded via the Wayback Machine. There are still holes in the data, but this should fill in some sheets for the previous 4 years before this scraper was created.

- **April 8th, 2026:** ICE now is housing the downloads in `https://www.ice.gov/file-download/download/public/`. Code has been adjusted accordingly.*

- **March 23rd, 2026:** Changed the URL in the scraper as ICE moved where the data is housed on their website.*

- **February 20th, 2026:** Added a license, `sheriff_script.R` to calculate the number of people policed by all Sheriff offices under 287g agreements, and `classification.R` to classify agencies by their agency type (i.e. Local Police Department, Federal Police Department, etc.)*

- ***July 7th, 2025:** Added a code and [resulting CSV](/agreements.csv) that merges the 287(G) data with agencies in the [Census of State and Local Law Enforcement Agencies (CSLLEA), 2018 (ICPSR 38771)](https://www.icpsr.umich.edu/web/NACJD/studies/38771). This allows us to merge the agency data with agency-centered datasets. Particularly, [`agreements.csv`](/agreements.csv) contains zipcodes, how many people the law enforcement agency polices, and what their operating budget is.* **NOTE:** This has been removed from this repository. 

- ***June 16th, 2025:** The `sheets` and `agreement` folders now only contain **new** data/documents to save storage.*

## Purpose

Law enforcement agencies are increasingly entering into agreements with ICE under the **287(g)** program, assisting in the deportation of immigrants from across the U.S., potentially facilitating hundreds of thousands of arrests. This program is supported by mandates like [Louisiana Executive Order Number JML 25-060: Project Geaux](https://interactive.wwltv.com/pdfs/Operation_GEAUX.pdf), which directs state law enforcement agencies to collaborate with ICE.

As relationships between ICE and local law enforcement become more common, it’s crucial to track which agencies are involved in the program. This repository provides a real-time overview of participating agencies and their respective agreements.


## File Structure

```
tracking-287g/
├── .github/
│   └── workflows/
│       └── run-script_final.yml   # GitHub Actions workflow automating the scraper
├── agreements/                    # PDF agreements between ICE and law enforcement agencies
├── analysis/                      # R scripts for analyzing and classifying the 287(g) data
├── archived_data/                 # Wayback Machine backfill (Jan 2021 onward)
│   ├── raw/                       # Raw HTML captures of the ICE page from the Wayback Machine
│   ├── before_2025/               # Data from when ICE published an HTML table
│   │   ├── sheets/                # Deduplicated CSV snapshots of the table over time
│   │   └── agreements/            # Agreement PDFs linked from the table
│   └── after_2025/                # Data from when ICE switched to downloadable .xlsx sheets
│       ├── sheets/                # Participating/pending .xlsx snapshots over time
│       └── agreements/            # Agreement files linked inside the .xlsx sheets
├── plots/                         # Output plots
├── sheets/                        # Excel files with participating and pending agency data
├── Tracking-287g.Rproj            # RStudio project file
├── archive.py                     # Backfills historical data from the Wayback Machine
├── deduplicate.py                 # Removes duplicate files and empty folders to save storage
├── script.py                      # Daily scraper that pulls 287(g) data from the ICE website
└── requirements.txt               # Python dependencies required to run the scraper
```

### Key files and folders
 
- **`script.py`**: The Python script responsible for scraping current 287(g) data from the ICE website. Run daily via GitHub Actions.
- **`archive.py`**: One-time backfill script that downloads historical captures, sheets, and agreements from the Wayback Machine and populates `archived_data/`.
- **`deduplicate.py`**: Utility that hashes files to remove duplicate agreements/sheets and prune empty directories.
- **`.github/workflows/run-script_final.yml`**: GitHub Actions workflow file used to automate execution of the scraper.
- **`requirements.txt`**: Lists all Python dependencies required to run the scrapers.

### Related Projects

- The [Recovered Factory](http://recoveredfactory.net/) published [Every active 287(g) agreement between local police and ICE](https://287g.recoveredfactory.net/), which analyzes 287(g) agreements, creating graphics, and estimating the % of people who live in communities with such agreements.
- The Markup published [Here’s Every Local Police Agency Enforcing for ICE](https://themarkup.org/tools/2025/04/16/law-enforcement-ice-cooperation-tracker), which has continued to track 287(g) agreements.
- The Immigrant Legal Resource Center maintains a [national map](https://www.ilrc.org/practitioners/national-map-287g-agreements) of 287(g) agreements along with resources to understand them.

## Setup

To use this repository, follow these steps:
 
### 1. Clone the repository
Clone the repository to your local machine:
 
```bash
git clone https://github.com/[your_username]/tracking-287g.git
```
 
### 2. Install dependencies
Ensure you have Python installed on your system. Then, install the necessary dependencies by running:
 
```bash
pip install -r requirements.txt
```
 
### 3. Run the scraper
To start the daily scraper, run the following command:
 
```bash
python script.py
```
 
### 4. (Optional) Backfill historical data
To backfill historical data from the Wayback Machine into `archived_data/`, run:
 
```bash
python archive.py
```
