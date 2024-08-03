# Web Scraping Projects

This repository contains two web scraping projects:
1. **Wikipedia Table Scraper**
2. **Amazon Data Scraper**

## Features

### Wikipedia Table Scraper

- Extract tables from any Wikipedia page URL.
- Save extracted data to CSV or JSON files.
- Handle tables with varying structures and complexities.

### Amazon Data Scraper

- Extract product details such as name, price, rating, and number of reviews.
- Save extracted data to CSV or JSON files.
- Handle pagination to scrape multiple pages of search results.

## Requirements

- Python 3.x
- BeautifulSoup4
- requests
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/web-scraping-projects.git
    cd web-scraping-projects
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Wikipedia Table Scraper

1. To scrape a table from a Wikipedia page, run the script with the page URL and table index as arguments:

    ```bash
    python scrape_wikipedia.py "https://en.wikipedia.org/wiki/Example_Page" 0
    ```

2. The scraped table will be saved as a CSV file in the `output` directory.

#### Configuration

- `scrape_wikipedia.py` script takes the following command-line arguments:
  - `url`: The URL of the Wikipedia page.
  - `table_index`: The index of the table to scrape (0 for the first table, 1 for the second, etc.).

#### Example

To scrape the first table from the Wikipedia page on "Python (programming language)":

```bash
python scrape_wikipedia.py "https://en.wikipedia.org/wiki/Python_(programming_language)" 0
