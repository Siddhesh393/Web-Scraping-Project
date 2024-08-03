# Web Scraping Projects

This repository contains two web scraping projects:
1. **Wikipedia Table Scraper**
2. **Reviews Data Scraper**

## Features

### Wikipedia Table Scraper

- Extract tables from any Wikipedia page URL.
- Save extracted data to CSV or JSON files.
- Handle tables with varying structures and complexities.

### Review Data Scraper

- Extract product details such as name, price, rating, and number of reviews.
- Save extracted data to CSV file.
- Handle pagination to scrape multiple pages of search results.

## Requirements

- Python 3.x
- BeautifulSoup4
- requests
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Siddhesh393/Web-Scraping-Project.git
    cd Web-Scraping-Project
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Wikipedia Table Scraper

1. Navigate to the `Wiki_Scraper` directory:

    ```bash
    cd Wiki_Scraper
    ```

2. To scrape a table from a Wikipedia page, run the script with the page URL and table index as arguments:

    ```bash
    python scrape_wikipedia.py "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov" 0
    ```

3. The scraped table will be saved as a CSV file in the `output` directory.

#### Configuration

- `scrape_wikipedia.py` script takes the following command-line arguments:
  - `target`: The type of data to retrieved used to access different functions of the script.
  - `url`: The URL of the Wikipedia page.
  - `output`: The name of the file to be saved in.


### Reviews Data Scraper

1. Navigate to the `Reviews_Scraper` directory within the repository:

    ```bash
    cd Reviews_Scraper
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```




