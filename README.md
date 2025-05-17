# Tracking 287(g)

This repository is designed to track the **287(g)** program, which includes participating and pending agencies. It scrapes data from the official [ICE 287(g) page](https://www.ice.gov/identify-and-arrest/287g) on a daily basis and stores the results in the `results` folder.

## Features
- **Automatic Scraping:** Scrapes the list of participating and pending agencies involved in the 287(g) program from the official ICE website.
- **Daily Updates:** The data is updated daily to ensure you have the most current information available.
- **Storage:** All scraped data is stored in the `results` folder.

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
- `scraper.py`: The main Python script responsible for scraping 287(g) data from the ICE website.
- `results/`: Directory that stores the output of the scraper, including the data files retrieved from the website.
- `requirements.txt`: Text file listing all Python dependencies required to run the scraper, ensuring consistent environments across different setups.
- `README.md`: Documentation file providing an overview of the project, instructions for setup, and usage guidelines.
