# Loading Libraries
import os
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from openpyxl import load_workbook
import csv
from datetime import datetime

# Page URL
URL = 'https://www.ice.gov/identify-and-arrest/287g'

# Getting page content
response = requests.get(URL)

# Parsing HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extracting participating link
participating = [
    a['href'] for a in soup.find_all('a', href=True)
    if "https://www.ice.gov/doclib/about/offices/ero/287g/participating" in a['href']
]

# Extracting pending link
pending = [
    a['href'] for a in soup.find_all('a', href=True)
    if "https://www.ice.gov/doclib/about/offices/ero/287g/pending" in a['href']
]

# Creating results folder
base_results_folder = "results"
if not os.path.exists(base_results_folder):
    os.makedirs(base_results_folder)

# Creating a timestamp  folder within the "results" folder
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_folder = os.path.join(base_results_folder, f"results_{timestamp}")
if not os.path.exists(results_folder):
    os.makedirs(results_folder)

# Making a function to read the excel data from the URL
def read_excel_from_url(url, folder):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        temp_file = BytesIO(response.content)
        wb = load_workbook(temp_file, data_only=True)
        sheet = wb.active
        file_name = os.path.join(folder, os.path.basename(url).replace(".xlsx", ".csv"))
        
        with open(file_name, mode='w', newline="", encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in sheet.iter_rows(values_only=True):
                csv_writer.writerow(row)
        
        print(f"Saved {file_name}")
    
    except Exception as e:
        print(f"Failed to download or save {url}: {e}")

# Reading participating data to results folder
for url in participating:
    read_excel_from_url(url, results_folder)

# Reading pending data to results folder
for url in pending:
    read_excel_from_url(url, results_folder)
