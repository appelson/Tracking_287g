# Importing packages
from wayback import WaybackClient
from datetime import datetime
import os, time
import re
import glob
import pandas as pd
import requests
import openpyxl

# Defining the URL to work on
URL = "https://www.ice.gov/identify-and-arrest/287g"

# Defining the parent director
ARCHIVED_DATA = "archived_data"

# Defining the raw HTML capture directory
RAW_DIR = os.path.join(ARCHIVED_DATA, "raw")

# Defining the before and after 2025 directories
BEFORE_2025 = os.path.join(ARCHIVED_DATA, "before_2025")
AFTER_2025 = os.path.join(ARCHIVED_DATA, "after_2025")

# Defining a cutoff for before 2025 and a cutoff for after 2025
CUTOFF = pd.Timestamp("2024-12-31 23:59:59")
CUTOFF_2025 = pd.Timestamp("2025-01-01 00:00:00")

# Defining the sheets and agreements subfolders
BEFORE_SHEETS = os.path.join(BEFORE_2025, "sheets")
BEFORE_AGREEMENTS = os.path.join(BEFORE_2025, "agreements")
AFTER_SHEETS = os.path.join(AFTER_2025, "sheets")
AFTER_AGREEMENTS = os.path.join(AFTER_2025, "agreements")

# ---------------------- Download all Wayback captures -------------------------

# Creating a function to download every wayback capture
def download_captures():

    # Creating the raw directory
    os.makedirs(RAW_DIR, exist_ok=True)

    # Opening a wayback client
    with WaybackClient() as client:

        # Getting all records until 7/1/2025
        records = list(client.search(URL, to_date=datetime(2025, 7, 1)))
        print(f"Found {len(records)} records")

        # Looping through each record
        for i, rec in enumerate(records, 1):

            # Timestamping the record and creating its path
            ts = rec.timestamp.strftime("%Y%m%d%H%M%S")
            path = os.path.join(RAW_DIR, f"{ts}.html")

            # Skipping already created files
            if os.path.exists(path):
                continue

            # Trying to download the memento
            try:
                mem = client.get_memento(rec)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(mem.text)
                print(f"[{i}/{len(records)}] OK {ts}")

            # Allowing for failures
            except Exception as e:
                print(f"[{i}/{len(records)}] FAIL {ts}: {e}")

            # Sleeping to not overwhelm wayback
            time.sleep(0.5)

# ----------------------- Extract tables before 2025 ---------------------------

# Creating a function to extract the table from a single HTML file < 2025
def extract_file(path):

    # Getting the filename and timestamp
    fname = os.path.basename(path)
    stamp = os.path.splitext(fname)[0]
    capture_date = pd.to_datetime(stamp, format="%Y%m%d%H%M%S", errors="coerce")

    # Making sure the capture date is < 2025
    if pd.isna(capture_date) or capture_date > CUTOFF:
        return []

    # Reading the HTML file
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Finding all rows
    rows = re.findall(r"<tr>(.*?)</tr>", html, re.DOTALL)
    out = []

    # Turning the rows into dictionaries
    for row in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)

        # There SHOULD only be 5 variables per table
        if len(cells) == 5:

            # Looking for all links in the last cell
            hrefs = re.findall(r'href="([^"]+)"', cells[4])

            # Defining the row
            out.append({
                "capture_date": capture_date,
                "capture_file": fname,
                "state": re.sub(r"<[^>]+>", "", cells[0]).strip(),
                "agency": re.sub(r"<[^>]+>", "", cells[1]).strip(),
                "support": re.sub(r"<[^>]+>", "", cells[2]).strip(),
                "signed": re.sub(r"<[^>]+>", "", cells[3]).strip(),
                "link": hrefs[0] if len(hrefs) > 0 else "",
                "addendum": hrefs[1] if len(hrefs) > 1 else "",
            })
    return out

# Creating a function to build a dataframe from ALL before-2025 files
def build_before_2025_df():

    # Defining empty lists
    all_rows, errors = [], []

    # Looping through all files
    for path in sorted(glob.glob(os.path.join(RAW_DIR, "*.html"))):

        # Trying to extract rows
        try:
            all_rows.extend(extract_file(path))

        # Allowing for failures
        except Exception as e:
            print(f"ERROR in {os.path.basename(path)}: {e}")
            errors.append((os.path.basename(path), str(e)))

    # Getting any errors and returning a dataframe of all rows
    print(f"Extraction errors: {len(errors)}")
    return pd.DataFrame(all_rows)

# --------------------- Save deduplicated before-2025 sheets --------------------

# Creating a function to save the deduplicated before-2025 sheets
def save_before_2025(df):

    # Copying the dataframe and getting a full timestamp string per capture
    df = df.copy()
    df["stamp"] = df["capture_date"].dt.strftime("%Y%m%d_%H%M%S")

    # Defining columns that define the actual data content
    content_cols = ["state", "agency", "support", "signed", "link", "addendum"]

    # Creating the before-2025 sheets folder
    os.makedirs(BEFORE_SHEETS, exist_ok=True)

    # Creating signatures for each dataset
    prev_signature = None
    for stamp in sorted(df["stamp"].unique()):
        group = df[df["stamp"] == stamp]

        # Defining the signature as the content columns of the group
        signature = group[content_cols].to_csv(index=False)

        # Skipping if identical to the previous capture
        if signature == prev_signature:
            print(f"Skipped {stamp} (duplicate)")
            continue

        # Saving the NEW dataset to the sheets folder
        out_path = os.path.join(BEFORE_SHEETS, f"{stamp}.csv")
        group.drop(columns="stamp").to_csv(out_path, index=False)
        print(f"Wrote {len(group)} rows to {out_path}")

        # Redefining the previous signature as the current signature
        prev_signature = signature

# --------------------- Download before-2025 agreement PDFs --------------------

# Creating a function to download the agreement PDFs linked in the tables
def download_pdfs(df):

    # Defining all unique links
    all_links = sorted(u for u in pd.concat([df["link"], df["addendum"]]).unique() if u)

    # Creating the before-2025 agreements folder
    os.makedirs(BEFORE_AGREEMENTS, exist_ok=True)

    # Defining a list of failed links
    failed = []

    # Trying to FIRST download the live links
    for i, url in enumerate(all_links, 1):
        fname = url.rsplit("/", 1)[-1].strip().replace(" ", "")
        dest = os.path.join(BEFORE_AGREEMENTS, fname)

        # Skipping already created files
        if os.path.exists(dest):
            continue

        # Trying to download the live link
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            with open(dest, "wb") as f:
                f.write(r.content)
            print(f"[{i}/{len(all_links)}] OK {fname}")

        # Allowing for failures
        except Exception as e:
            failed.append(url)
            print(f"[{i}/{len(all_links)}] FAIL {fname}: {e}")

    # Trying to download the associated wayback links for any that failed
    still_failed = []
    with WaybackClient() as client:
        for i, url in enumerate(failed, 1):
            fname = url.rsplit("/", 1)[-1].strip().replace(" ", "")
            dest = os.path.join(BEFORE_AGREEMENTS, fname)

            # Searching wayback and downloading
            try:
                records = list(client.search(url, filter_field="statuscode:200"))

                # Recording links with no wayback snapshots
                if not records:
                    still_failed.append(url)
                    print(f"[{i}/{len(failed)}] NONE {fname}")
                    continue

                # Downloading the memento
                mem = client.get_memento(records[0])
                with open(dest, "wb") as f:
                    f.write(mem.content)
                print(f"[{i}/{len(failed)}] WAYBACK {fname}")

            # Allowing for failures
            except Exception as e:
                still_failed.append(url)
                print(f"[{i}/{len(failed)}] FAIL {fname}: {e}")

    # Number of links still failing
    print(f"Still failed: {len(still_failed)}")
    return still_failed

# ------------------ Extract xlsx URLs from 2025+ captures ------------------

# Creating a function to grab participating + pending xlsx links from > 2025 files
def extract_xlsx_urls():

    # Defining empty lists
    rows, errors = [], []

    # Looping through all files
    for path in sorted(glob.glob(os.path.join(RAW_DIR, "*.html"))):
        fname = os.path.basename(path)
        stamp = os.path.splitext(fname)[0]
        capture_date = pd.to_datetime(stamp, format="%Y%m%d%H%M%S", errors="coerce")

        # Ensuring that the data comes > 2025
        if pd.isna(capture_date) or capture_date < CUTOFF_2025:
            continue

        # Trying to read the HTML and extract the xlsx links
        try:
            with open(path, "r", encoding="utf-8") as f:
                html = f.read()

            # Defining the participating and pending agencies files
            participating = re.findall(r'href="([^"]*participatingAgencies[^"]*\.xlsx)"', html)
            pending = re.findall(r'href="([^"]*pendingAgencies[^"]*\.xlsx)"', html)

            # Returning the links, file, and date
            rows.append({
                "capture_date": capture_date,
                "capture_file": fname,
                "participating": participating[0] if participating else "",
                "pending": pending[0] if pending else "",
            })

        # Allowing for failures
        except Exception as e:
            print(f"ERROR in {fname}: {e}")
            errors.append((fname, str(e)))

    # Getting the XLSX dataframe and any errors
    df_xlsx = pd.DataFrame(rows)
    print(f"xlsx extraction errors: {len(errors)}")
    return df_xlsx

# ------------------ Download after-2025 xlsx sheets via Wayback ------------------

# Creating a function to download every xlsx snapshot via wayback
def download_xlsx(df_xlsx):

    # Creating the after-2025 sheets folder
    os.makedirs(AFTER_SHEETS, exist_ok=True)

    # Defining all unique xlsx links
    urls = sorted(u for u in pd.concat([df_xlsx["participating"], df_xlsx["pending"]]).unique() if u)

    # Normalizing relative links to absolute ICE URLs
    abs_urls = []
    for u in urls:
        if u.startswith("http"):
            abs_urls.append(u)
        else:
            abs_urls.append("https://www.ice.gov" + (u if u.startswith("/") else "/" + u))
    print(f"{len(abs_urls)} unique xlsx URLs to fetch")

    # Defining lists of downloaded and missed files
    got, missed = [], []

    # Opening a wayback client
    with WaybackClient() as client:

        # Looping through each xlsx URL
        for i, url in enumerate(abs_urls, 1):

            # Searching wayback for all snapshots of this xlsx URL
            try:
                records = list(client.search(url, filter_field="statuscode:200"))

                # Recording URLs with no wayback snapshots
                if not records:
                    missed.append((url, "no snapshots"))
                    print(f"[{i}/{len(abs_urls)}] NONE {url}")
                    continue

                # Looping through every snapshot to capture changes over time
                for rec in records:
                    ts = rec.timestamp.strftime("%Y%m%d_%H%M%S")
                    base = url.rsplit("/", 1)[-1]
                    dest = os.path.join(AFTER_SHEETS, f"{ts}_{base}")

                    # Skipping already created files
                    if os.path.exists(dest):
                        got.append(dest)
                        continue

                    # Trying to download the memento
                    try:
                        mem = client.get_memento(rec)

                        # Verifying it is a real xlsx
                        if mem.content[:2] != b"PK":
                            missed.append((f"{ts}_{base}", "not xlsx"))
                            print(f"[{i}/{len(abs_urls)}] BAD {ts}_{base} (not xlsx)")
                            continue

                        # Writing the xlsx file
                        with open(dest, "wb") as f:
                            f.write(mem.content)
                        print(f"[{i}/{len(abs_urls)}] OK {ts}_{base} ({len(mem.content):,} bytes)")
                        got.append(dest)

                    # Allowing for failures
                    except Exception as e:
                        missed.append((f"{ts}_{base}", str(e)))
                        print(f"[{i}/{len(abs_urls)}] FAIL {ts}_{base}: {e}")

                    # Sleeping to not overwhelm wayback
                    time.sleep(0.5)

            # Allowing for search failures
            except Exception as e:
                missed.append((url, str(e)))
                print(f"[{i}/{len(abs_urls)}] SEARCH FAIL {url}: {e}")

    # Printing the totals and any missed files
    print(f"\nGot {len(got)}, missed {len(missed)}")
    for item, msg in missed:
        print(f"  {msg}: {item}")
    return got, missed
  
  
# --------------- Download after-2025 agreements from saved xlsx ---------------
  
# Creating a function to download all unique agreements linked inside the saved xlsx
def download_after_2025_agreements():

    # Creating the after-2025 agreements folder
    os.makedirs(AFTER_AGREEMENTS, exist_ok=True)

    # Defining a set of all unique hyperlinks across every saved xlsx
    hyperlinks = set()

    # Looping through every saved participating xlsx (these hold the agreement links)
    for path in sorted(glob.glob(os.path.join(AFTER_SHEETS, "*participatingAgencies*.xlsx"))):
        fname = os.path.basename(path)

        # Trying to read the workbook
        try:
            wb = openpyxl.load_workbook(path)
            sheet = wb.active
        except Exception as e:
            print(f"Could not open {fname}: {e}")
            continue

        # Collecting the hyperlink from each row
        for row in sheet.iter_rows(min_col=1, max_col=1000):
            if len(row) < 7:
                continue
            hyperlink = row[6].hyperlink.target if row[6].hyperlink else None
            if hyperlink:
                hyperlinks.add(hyperlink)

    # Sorting the unique links
    hyperlinks = sorted(hyperlinks)
    print(f"Found {len(hyperlinks)} unique agency agreement links")

    # Defining a list of failed links
    failed = []

    # Looping through each unique link
    for i, hyperlink in enumerate(hyperlinks, 1):

        # Preferring the URL basename for the filename
        out_name = os.path.basename(hyperlink.split("?")[0]).strip().replace(" ", "")
        dest = os.path.join(AFTER_AGREEMENTS, out_name)

        # Skipping already created files
        if os.path.exists(dest):
            continue

        # Trying to download the live agreement file
        try:
            time.sleep(1)
            r = requests.get(hyperlink, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
            if r.status_code == 200:

                # Preferring the Content-Disposition filename if present
                cd = r.headers.get("Content-Disposition", "")
                if "filename=" in cd:
                    out_name = cd.split("filename=")[-1].strip().strip('"').strip("'")
                    dest = os.path.join(AFTER_AGREEMENTS, out_name)

                # Falling back to a default name if the URL had none
                if not out_name or "." not in out_name:
                    out_name = f"agreement_{i}"
                    dest = os.path.join(AFTER_AGREEMENTS, out_name)

                # Writing the agreement file
                with open(dest, "wb") as f:
                    f.write(r.content)
                print(f"[{i}/{len(hyperlinks)}] OK {out_name}")

            # Recording non-200 responses
            else:
                print(f"[{i}/{len(hyperlinks)}] HTTP {r.status_code} for {hyperlink}")
                failed.append(hyperlink)

        # Allowing for failures
        except Exception as e:
            print(f"[{i}/{len(hyperlinks)}] Exception for {hyperlink}: {e}")
            failed.append(hyperlink)

    # Logging failed downloads
    if failed:
        failed_log_path = os.path.join(AFTER_AGREEMENTS, "failed_downloads.txt")
        with open(failed_log_path, "w") as log_file:
            for failure in failed:
                log_file.write(f"{failure}\n")
        print(f"{len(failed)} failed downloads logged to {failed_log_path}")
    print("Done.")

# --------------------------- Run --------------------------------------------

# Downloading all wayback captures
download_captures()

# Building and saving the deduplicated before-2025 sheets
df = build_before_2025_df()
save_before_2025(df)

# Downloading the before-2025 agreement PDFs
download_pdfs(df)

# Extracting and downloading the after-2025 xlsx sheets
df_xlsx = extract_xlsx_urls()
download_xlsx(df_xlsx)
download_after_2025_agreements()
