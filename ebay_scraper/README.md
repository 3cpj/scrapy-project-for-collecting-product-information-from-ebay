# eBay Scraper

This project is a web scraper built with Scrapy to extract product information from eBay search results.

## Features

- Scrapes product details including Name, Price, Shipping Fee, and Location
- Saves data in JSON format
- Respects eBay's robots.txt rules
- Implements a delay between requests to avoid overloading the server

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ebay_scraper.git
   cd ebay_scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the spider and scrape eBay for "large language model" products:

```
scrapy crawl ebay -a query="large language model"
```

This will save the scraped data to `data/output.json`.     

## RUN

```
scrapy crawl ebay -s LOG_LEVEL=DEBUG
```