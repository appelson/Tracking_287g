# Tracking 287(g)

This repository downloads data from the **287(g)** program and organizes it to be used by journalists, advocates, and the public. The scraper runs daily, extracting data from the official [ICE 287(g) page](https://www.ice.gov/identify-and-arrest/287g). The data is saved in two main folders:

- **`agreements/`**: Contains PDFs of all 287(g) agreements between law enforcement agencies and ICE, categorized by download date/time, state, and agency.
- **`sheets/`**: Stores Excel files listing participating and pending agencies, as published on the ICE website, categorized by download date/time.

### *Note*
This project was created in my personal capacity. Should you have any questions or suggestions for other public immigration data you would like to see tracked, you can contact me at elijahappelson@gmail.com. 

## Agency Counts
### Pending Agencies Count:

 1. FLORIDA         | ████████████████████████████████████████ 23
 2. GEORGIA         | ███████████████████ 11
 3. TEXAS           | ████████████ 7
 4. ALABAMA         | ██████████ 6
 5. TENNESSEE       | ██████ 4
 6. KANSAS          | ███ 2
 7. NEVADA          | ███ 2
 8. OKLAHOMA        | ███ 2
 9. WYOMING         | ███ 2
10. ARIZONA         | █ 1
11. MARYLAND        | █ 1
12. MICHIGAN        | █ 1
13. MINNESOTA       | █ 1
14. MISSOURI        | █ 1
15. MONTANA         | █ 1
16. PENNSYLVANIA    | █ 1
17. VIRGINIA        | █ 1
18. WISCONSIN       | █ 1

### Participating Agencies Count:

 1. FLORIDA         | ████████████████████████████████████████ 270
 2. TEXAS           | ████████████ 87
 3. GEORGIA         | ███ 23
 4. NORTH CAROLINA  | ███ 21
 5. VIRGINIA        | ██ 15
 6. KENTUCKY        | ██ 15
 7. OKLAHOMA        | ██ 15
 8. SOUTH CAROLINA  | ██ 14
 9. WISCONSIN       | █ 13
10. NEW HAMPSHIRE   | █ 11
11. PENNSYLVANIA    | █ 11
12. ALABAMA         | █ 9
13. ARIZONA         | █ 7
14. MINNESOTA       | █ 7
15. MARYLAND        | █ 7
16. TENNESSEE       | █ 7
17. OHIO            |  6
18. KANSAS          |  6
19. NEW YORK        |  6
20. WYOMING         |  6
21. NORTH DAKOTA    |  5
22. INDIANA         |  4
23. MISSOURI        |  4
24. IDAHO           |  4
25. MICHIGAN        |  4
26. LOUISIANA       |  3
27. MONTANA         |  3
28. UTAH            |  3
29. ALASKA          |  2
30. ARKANSAS        |  2
31. NEBRASKA        |  2
32. NEVADA          |  2
33. SOUTH DAKOTA    |  2
34. COLORADO        |  1
35. IOWA            |  1
36. MISSISSIPPI     |  1
37. MASSACHUSETTS   |  1
38. NEW MEXICO      |  1
39. MAINE           |  1
40. WEST VIRGINIA   |  1

## Purpose

Law enforcement agencies are increasingly entering into agreements with ICE under the **287(g)** program, assisting in the deportation of immigrants from across the U.S. This program is supported by mandates like [Louisiana Executive Order Number JML 25-060: Project Geaux](https://interactive.wwltv.com/pdfs/Operation_GEAUX.pdf), which directs state law enforcement agencies to collaborate with ICE.

As mandates like this continue to grow, it’s crucial to track which agencies are involved in the program, especially as the Federal Government continues to make data harder to access. This repository provides a real-time overview of participating agencies and their respective agreements.

### *Note*
The Immigration Legal Resource Center maintains a [national map](https://www.ilrc.org/practitioners/national-map-287g-agreements) of 287(g) agreements along with resources to  understand them. 

## Setup

To use this repository, follow these steps:

### 1. Clone the repository
Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/tracking-287g.git
```

### 2. Install dependencies
Ensure you have Python installed on your system. Then, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
````
### 3. Run the scraper
To start the scraper, run the following command:

```bash
python scraper.py
```

## File Structure

- `.github/workflows/run_scripts.yaml`: GitHub Actions workflow file used for automating the execution of the scraper script.
- `scraper.py`: The Python script responsible for scraping 287(g) data from the ICE website.
- `agreements/`: Directory that stores the PDF agreements between ICE and law enforcement agencies.
- `sheets/`: Directory that stores the excel files with data on participating and pending agreements between ICE and law enforcement agencies.
- `requirements.txt`: Text file listing all Python dependencies required to run the scraper.
- `README.md`: This file.
