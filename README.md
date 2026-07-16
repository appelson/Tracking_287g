# Tracking 287(g)

This repository downloads data and agreements from the **287(g)** program and organizes them to be used by journalists, advocates, and the public. The scraper runs daily, extracting data from the official [ICE 287(g) page](https://www.ice.gov/identify-and-arrest/287g).

**The data is saved in three main folders:**

- **`agreements/`**: PDFs of all 287(g) agreements between law enforcement agencies and ICE, organized by download date/time, state, and agency.
- **`sheets/`**: Excel files listing participating and pending agencies, as published on the ICE website, organized by download date/time.
- **`archived_data/`**: 287(g) sheets and agreements backfilled from the [Wayback Machine](http://web.archive.org/), covering January 2021 up to when this scraper was created. This fills in *some* of the data missing from the years before this project existed. It is split into `before_2025/` (when ICE published the data as an HTML table on its website) and `after_2025/` (when ICE switched to downloadable `.xlsx` sheets), plus a `raw/` folder holding the HTML captures used to build both. To save space, the `sheets/` folders contain only snapshots that differ from the preceding date. Identical consecutive captures are dropped, so the data is complete but without consecutive duplicates. See [Limitations](#limitations) for important caveats about completeness.

### *Note*
This project was created in my personal capacity. Should you have any questions or suggestions for other public immigration data you would like to see tracked, you can contact me at **elijahappelson@gmail.com**.

## Updates
- ***June 8th, 2026:** Added archived data backfilled from the Wayback Machine, covering roughly the four years before this scraper existed. There are still holes in the data, but this fills in many of the earlier sheets.*

- ***April 8th, 2026:** ICE now houses the downloads at `https://www.ice.gov/file-download/download/public/`. Code has been adjusted accordingly.*

- ***March 23rd, 2026:** Changed the URL in the scraper, as ICE moved where the data is housed on their website.*

- ***February 20th, 2026:** Added a license, `sheriff_script.R` to calculate the number of people policed by all Sheriff offices under 287(g) agreements, and `classification.R` to classify agencies by type (e.g., Local Police Department, Federal Police Department, etc.).*

- ***July 7th, 2025:** Added code and a resulting CSV that merged the 287(g) data with agencies in the [Census of State and Local Law Enforcement Agencies (CSLLEA), 2018 (ICPSR 38771)](https://www.icpsr.umich.edu/web/NACJD/studies/38771), allowing the agency data to be joined with agency-centered datasets. The CSV contained zipcodes, the population each agency polices, and its operating budget.* **NOTE:** This has since been removed from the repository.

- ***June 16th, 2025:** The `sheets/` and `agreements/` folders now contain only **new** data/documents, to save storage.*

<!-- STATE_BREAKDOWN:START -->
## Statewide Breakdown

Number of 287(g) agreements per state, by support type. *Last updated: 2026-07-16 17:04 UTC — 41 states, 2127 total agreements (source: `participatingAgencies07142026pm.xlsx`).*

| State | Task Force Model | Warrant Service Officer | Jail Enforcement Model | Total |
| --- | ---: | ---: | ---: | ---: |
| Texas | 263 | 148 | 54 | 465 |
| Florida | 274 | 65 | 10 | 349 |
| Arkansas | 80 | 35 | 14 | 129 |
| Missouri | 102 | 10 | 2 | 114 |
| Pennsylvania | 106 | 3 | 0 | 109 |
| Tennessee | 33 | 56 | 10 | 99 |
| Oklahoma | 76 | 7 | 5 | 88 |
| Georgia | 37 | 27 | 17 | 81 |
| Alabama | 53 | 9 | 10 | 72 |
| Louisiana | 49 | 10 | 6 | 65 |
| South Carolina | 36 | 14 | 3 | 53 |
| Mississippi | 43 | 5 | 4 | 52 |
| Kansas | 18 | 28 | 4 | 50 |
| Kentucky | 45 | 2 | 3 | 50 |
| Indiana | 33 | 7 | 3 | 43 |
| West Virginia | 37 | 1 | 0 | 38 |
| Virginia | 23 | 5 | 1 | 29 |
| North Carolina | 7 | 18 | 3 | 28 |
| New Hampshire | 23 | 0 | 0 | 23 |
| Wisconsin | 0 | 18 | 5 | 23 |
| Ohio | 17 | 4 | 1 | 22 |
| Wyoming | 10 | 7 | 2 | 19 |
| Utah | 6 | 8 | 4 | 18 |
| North Dakota | 10 | 4 | 1 | 15 |
| Idaho | 4 | 8 | 1 | 13 |
| New York | 6 | 6 | 1 | 13 |
| Minnesota | 6 | 3 | 1 | 10 |
| Arizona | 1 | 4 | 5 | 10 |
| South Dakota | 4 | 3 | 1 | 8 |
| Nebraska | 6 | 0 | 2 | 8 |
| Michigan | 4 | 3 | 0 | 7 |
| Montana | 4 | 2 | 0 | 6 |
| Nevada | 0 | 4 | 1 | 5 |
| Iowa | 2 | 0 | 0 | 2 |
| New Mexico | 0 | 2 | 0 | 2 |
| Alaska | 0 | 2 | 0 | 2 |
| New Hamsphire | 2 | 0 | 0 | 2 |
| Northern Mariana Islands | 1 | 0 | 1 | 2 |
| Colorado | 0 | 0 | 1 | 1 |
| Guam | 1 | 0 | 0 | 1 |
| Massachusetts | 0 | 0 | 1 | 1 |
| **All states** | **1422** | **528** | **177** | **2127** |

<!-- STATE_BREAKDOWN:END -->
## Purpose

Law enforcement agencies are increasingly entering into agreements with ICE under the **287(g)** program, assisting in the deportation of immigrants from across the U.S. and potentially facilitating hundreds of thousands of arrests. The program is reinforced by mandates like [Louisiana Executive Order Number JML 25-060: Project Geaux](https://interactive.wwltv.com/pdfs/Operation_GEAUX.pdf), which directs state law enforcement agencies to collaborate with ICE.

As relationships between ICE and local law enforcement become more common, it's crucial to track which agencies are involved. This repository provides a real-time overview of participating agencies and their respective agreements.

## Limitations

The archived data is incomplete for a few reasons:

- **HTML vs. XLSX formats**: Sheets in `before_2025/` are extracted from the HTML table ICE published directly on its website (can be found in `archived_data/raw`), while `after_2025/` sheets come from the downloadable `.xlsx` files ICE later switched to. The two are structured differently.
- **Overwritten links (Roughly January - March 2025)**: ICE initially reused a single URL for each new participating/pending sheet, overwriting the previous file each time. The Wayback Machine didn't capture every overwrite, so many `after_2025/` sheets are missing. 
- **Unarchived files.** Some Excel files were never captured by the Wayback Machine and no longer exist anywhere, so they can't be recovered.

The full set of sheets, including the consecutive duplicates dropped from `archived_data/`, or a single combined CSV of all of them, is available on request.

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
│   │   └── sheets/                # Deduplicated snapshots of the table over time
│   └── after_2025/                # Data from when ICE switched to downloadable .xlsx sheets
│       └── sheets/                # Participating/pending .xlsx snapshots over time
├── plots/                         # Output plots
├── sheets/                        # Excel files with participating and pending agency data
├── Tracking-287g.Rproj            # RStudio project file
├── archive.py                     # Backfills historical data from the Wayback Machine
├── deduplicate.py                 # Removes duplicate files and empty folders to save storage
├── script.py                      # Daily scraper that pulls 287(g) data from the ICE website
└── requirements.txt               # Python dependencies required to run the scraper
```

### Key files and folders

- **`script.py`**: Scrapes current 287(g) data from the ICE website. Run daily via GitHub Actions.
- **`archive.py`**: One-time backfill script that downloads historical captures, sheets, and agreements from the Wayback Machine and populates `archived_data/`.
- **`deduplicate.py`**: Utility that hashes files to remove duplicate agreements/sheets and prune empty directories.
- **`.github/workflows/run-script_final.yml`**: GitHub Actions workflow that automates execution of the scraper.
- **`requirements.txt`**: Lists all Python dependencies required to run the scrapers.

### Related Projects

- The [Recovered Factory](http://recoveredfactory.net/) published [Every active 287(g) agreement between local police and ICE](https://287g.recoveredfactory.net/), which analyzes 287(g) agreements, creates graphics, and estimates the percentage of people living in communities with such agreements.
- The Markup published [Here's Every Local Police Agency Enforcing for ICE](https://themarkup.org/tools/2025/04/16/law-enforcement-ice-cooperation-tracker), which continues to track 287(g) agreements.
- The Immigrant Legal Resource Center maintains a [national map](https://www.ilrc.org/practitioners/national-map-287g-agreements) of 287(g) agreements, along with resources to understand them.

## Setup

To use this repository, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/[your_username]/tracking-287g.git
```

### 2. Install dependencies

Ensure you have Python installed, then install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the scraper

```bash
python script.py
```

### 4. (Optional) Backfill historical data

To backfill historical data from the Wayback Machine into `archived_data/`:

```bash
python archive.py
```
