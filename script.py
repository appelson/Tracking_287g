# Loading Libraries
import os
import sys
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import openpyxl


# ------------------- Step 1: Downloading the Excel Files ---------------------

# Base 287g Page URL
URL = 'https://www.ice.gov/identify-and-arrest/287g'

# Getting page content
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.content, 'html.parser')

# Match links by anchor text (case-insensitive) — robust to href URL changes
def find_links_by_text(soup, keyword):
    results = []
    for a in soup.find_all('a', href=True):
        text = (a.get_text() or '').lower()
        if keyword.lower() in text:
            href = a['href']
            # Ensure absolute URL
            if href.startswith('/'):
                href = 'https://www.ice.gov' + href
            results.append(href)
    return results

participating = find_links_by_text(soup, 'participating agencies')
pending = find_links_by_text(soup, 'pending agencies')

# Log what was found
print(f"Found {len(participating)} participating link(s): {participating}")
print(f"Found {len(pending)} pending link(s): {pending}")

# Abort early with a clear message if nothing found
if not participating:
    print("\nERROR: No participating agencies link found on the ICE page.")
    print("Here are all links found on the page:")
    for a in soup.find_all('a', href=True):
        print(f"  [{a.get_text().strip()}] {a['href']}")
    sys.exit(1)

# Creating the "sheets" folder
base_results_folder = "sheets"
os.makedirs(base_results_folder, exist_ok=True)

# Creating a timestamped subfolder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_folder = os.path.join(base_results_folder, f"sheets_{timestamp}")
os.makedirs(results_folder, exist_ok=True)

# Function to download and save Excel files
def download_excel_from_url(url, folder, label="file"):
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()

        # Try to get filename from Content-Disposition header first
        cd = r.headers.get('Content-Disposition', '')
        if 'filename=' in cd:
            file_name_only = cd.split('filename=')[-1].strip().strip('"').strip("'")
        else:
            # Fall back to last segment of URL, default to label-based name
            file_name_only = os.path.basename(url.split('?')[0])
            if not file_name_only or '.' not in file_name_only:
                file_name_only = f"{label}.xlsx"

        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, file_name_only)
        with open(file_path, 'wb') as f:
            f.write(r.content)
        print(f"Downloaded: {file_path}")
        return file_path

    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return None

# Download participating and pending files
downloaded_participating = []
for url in participating:
    path = download_excel_from_url(url, results_folder, label="participating")
    if path:
        downloaded_participating.append(path)

for url in pending:
    download_excel_from_url(url, results_folder, label="pending")

if not downloaded_participating:
    print("ERROR: Failed to download any participating agencies file.")
    sys.exit(1)


# --------------------- Step 2: Downloading the Agreements ---------------------

# Reading the excel document as a workbook
file_path = downloaded_participating[0]
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

# Defining empty lists
hyperlinks = []
states = []
agencies = []
failed = []

# Filling the lists
for row in sheet.iter_rows(min_col=1, max_col=1000):
    if len(row) < 7:
        continue
    state = row[0].value
    agency_name = row[1].value
    hyperlink = row[6].hyperlink.target if row[6].hyperlink else None

    if hyperlink and state and agency_name:
        hyperlinks.append(hyperlink)
        states.append(state)
        agencies.append(agency_name)

print(f"Found {len(hyperlinks)} agency agreement links.")

# Creating an "agreements" folder
documents_folder = "agreements"
os.makedirs(documents_folder, exist_ok=True)

# Creating a timestamped subfolder
timestamp_folder = os.path.join(documents_folder, f"agreements_{timestamp}")
os.makedirs(timestamp_folder, exist_ok=True)

# Looping through state, agency, hyperlink combinations
for i, hyperlink in enumerate(hyperlinks):

    state = states[i]
    agency_name = agencies[i]

    # Clean state and agency names for use as folder names
    safe_state_name = state.replace(' ', '_')
    safe_agency_name = agency_name.replace('/', '_').replace('\\', '_').replace(' ', '_')

    # Create state and agency folders
    state_folder = os.path.join(timestamp_folder, safe_state_name)
    os.makedirs(state_folder, exist_ok=True)

    agency_folder = os.path.join(state_folder, safe_agency_name)
    os.makedirs(agency_folder, exist_ok=True)

    # Download the agreement file
    try:
        time.sleep(1)
        r = requests.get(hyperlink, headers={"User-Agent": "Mozilla/5.0"})

        if r.status_code == 200:
            # Prefer Content-Disposition filename, fall back to URL basename
            cd = r.headers.get('Content-Disposition', '')
            if 'filename=' in cd:
                fname = cd.split('filename=')[-1].strip().strip('"').strip("'")
            else:
                fname = os.path.basename(hyperlink.split('?')[0])
                if not fname or '.' not in fname:
                    fname = f"{safe_agency_name}_agreement"

            file_name = os.path.join(agency_folder, fname)
            with open(file_name, 'wb') as f:
                f.write(r.content)
        else:
            print(f"HTTP {r.status_code} for {hyperlink}")
            failed.append(hyperlink)

    except Exception as e:
        print(f"Exception for {hyperlink}: {e}")
        failed.append(hyperlink)

# Log failed downloads
if failed:
    failed_log_path = os.path.join(timestamp_folder, "failed_downloads.txt")
    with open(failed_log_path, 'w') as log_file:
        for failure in failed:
            log_file.write(f"{failure}\n")
    print(f"{len(failed)} failed downloads logged to {failed_log_path}")

print("Done.")
