# Books Scraper

Scrapes all 1000 books from [books.toscrape.com](https://books.toscrape.com) and saves them to a CSV file.

## What it does

- Scrapes all 50 pages automatically
- Extracts: book title, price, and star rating
- Saves output to `books.csv`

## Requirements

```bash
pip install playwright pandas
playwright install firefox
```

## Usage

```bash
python books_scraper.py
```

## Output

A `books.csv` file with 1000 rows:

| name | price | Star-rating |
|------|-------|-------------|
| A Light in the Attic | £51.77 | Three |
| Tipping the Velvet | £53.74 | One |
| ... | ... | ... |
