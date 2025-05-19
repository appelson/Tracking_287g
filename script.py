# Loading Libraries
import os
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import openpyxl


# ------------------- Step 1: Downloading the Excel Files ---------------------

# Base 287g Page URL
URL = 'https://www.ice.gov/identify-and-arrest/287g'

# Getting page content
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting the participating agencies link
participating = [
    a['href'] for a in soup.find_all('a', href=True)
    if "https://www.ice.gov/doclib/about/offices/ero/287g/participating" in a['href']
]

# Extracting the pending agencies link
pending = [
    a['href'] for a in soup.find_all('a', href=True)
    if "https://www.ice.gov/doclib/about/offices/ero/287g/pending" in a['href']
]

# Creating the "sheets" document
base_results_folder = "sheets"
if not os.path.exists(base_results_folder):
    os.makedirs(base_results_folder)

# Creating a timestamp "sheets" file within "sheets"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_folder = os.path.join(base_results_folder, f"sheets_{timestamp}")
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# Function to download and safe the excel files
def download_excel_from_url(url, folder):
    try:
        response = requests.get(url)
        os.makedirs(folder, exist_ok=True)
        file_name = os.path.join(folder, os.path.basename(url))

        # Saving the excel file
        with open(file_name, mode='wb') as excel_file:
            excel_file.write(response.content)

    except Exception as e:
        print(f"Failed")

# Downloading the participating and pending files
for url in participating:
    download_excel_from_url(url, results_folder)

for url in pending:
    download_excel_from_url(url, results_folder)


# --------------------- Step 2: Downloading the Agreements ---------------------

# Reading the excel document in as a workbook
file_path = os.path.join(results_folder, os.path.basename(participating[0]))
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

column_letter = 'G' # This is where the hyperlinks are

# Defining empty lists
hyperlinks = []
states = []
agencies = []
failed = []

# Filling the lists
for row in sheet.iter_rows(min_col=1, max_col=1000):
    state = row[0].value
    agency_name = row[1].value
    hyperlink = row[6].hyperlink.target if row[6].hyperlink else None

    if hyperlink and state and agency_name:
        hyperlinks.append(hyperlink)
        states.append(state)
        agencies.append(agency_name)

# Creating an "agreements" folder
documents_folder = "agreements"
os.makedirs(documents_folder, exist_ok=True)

# Creating a timestamped "agreements" folder inside "agreements" 
timestamp_folder = os.path.join(documents_folder, f"agreements_{timestamp}")
os.makedirs(timestamp_folder, exist_ok=True)

# Looping through state, agency, hyperlink combinations
for i, hyperlink in enumerate(hyperlinks):

    state = states[i]
    agency_name = agencies[i]
    
    # Ensuring the state and agency names are clean
    safe_state_name = state.replace(' ', '_')
    safe_agency_name = agency_name.replace('/', '_').replace('\\', '_').replace(' ', '_')

    # Creating a "state" folder
    state_folder = os.path.join(timestamp_folder, safe_state_name)
    os.makedirs(state_folder, exist_ok=True)

    # Creating an "agency" folder within the state folder
    agency_folder = os.path.join(state_folder, safe_agency_name)
    os.makedirs(agency_folder, exist_ok=True)

    # Downloading the hyperlinks into the respective agency
    try:
        time.sleep(1)
        response = requests.get(hyperlink)

        if response.status_code == 200:
            file_name = os.path.join(agency_folder, os.path.basename(hyperlink))
            with open(file_name, 'wb') as f:
                f.write(response.content)
        else:
            failed.append(hyperlink)

    except Exception as e:
        failed.append(hyperlink)

# Creating a log of failed hyperlinks
if failed:
    failed_log_path = os.path.join(timestamp_folder, "failed_downloads.txt")
    with open(failed_log_path, 'w') as log_file:
        for failure in failed:
            log_file.write(f"{failure}\n")
