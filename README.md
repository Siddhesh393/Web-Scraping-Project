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
  - `url`: The URL of the Wikipedia page.
  - `table_index`: The index of the table to scrape (0 for the first table, 1 for the second, etc.).

#### Example

To scrape the first table from the Wikipedia page on "Khabib Nurmagomedov":

```bash
python scrape_wikipedia.py "https://en.wikipedia.org/wiki/Khabib_Nurmagomedov" 0



### Reviews Data Scraper

This project is a web scraper designed to extract product data from Ecommerce Website, including product names, prices, ratings, and reviews.

#### Features

- Extract product details such as name, price, rating, and number of reviews.
- Save extracted data to CSV or JSON files.
- Handle pagination to scrape multiple pages of search results.

#### Requirements

- Python 3.x
- BeautifulSoup4
- requests
- pandas

#### Installation

1. Navigate to the `Reviews_Scraper` directory within the repository:

    ```bash
    cd Reviews_Scraper
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

#### Usage

1. To scrape product data from Ecommerce Website, run the script:

    ```bash
    python scrape_reviews.py
    ```

2. The scraped data will be saved as a CSV file in the `output` directory.

#### Configuration

- `scrape_reviews.py` script takes the following command-line arguments:
  - `query`: The search query for the products you want to scrape.

#### Example

To scrape data for keyboards from Reviews:

```bash
python scrape_reviews.py "keyboards"

