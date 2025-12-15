# 🧩 Web Scraping Multiple HTML Tables with BeautifulSoup

## Project Overview

This project demonstrates a complete web scraping and data preparation workflow using Python.  
The main goal is to extract structured data from **multiple HTML tables**, clean and standardize the data, merge related datasets, and generate a final dataset ready for analysis.

The project focuses on tourism statistics of major cities, enriched with reference links and image URLs.

## Project Objectives

- Scrape data from multiple HTML tables using BeautifulSoup
- Extract tourism statistics for major cities
- Clean and convert numeric values into analysis-ready formats
- Safely handle missing or optional HTML elements
- Merge multiple datasets into a single unified table
- Export the final cleaned dataset as a CSV file

## Data Description

The dataset includes the following information:

- City – Name of the city  
- Country – Country of the city  
- Visitors (Millions) – Number of visitors  
- Wikipedia_URL – Reference link for each city  
- Image_URL – Image link associated with each city  

All data is extracted from structured HTML content.  
No external APIs are used in this project.

## Tools & Libraries Used

- Python
- BeautifulSoup (bs4)
- Pandas


## Project Structure

```text
Web-Scraping-Multiple-HTML-Tables-with-BeautifulSoup/
│
├── city_tourism_web_scraping.ipynb
├── final_city_tourism_dataset.csv
└── README.md



## Project Workflow

1. Parse raw HTML content using BeautifulSoup  
2. Extract data from multiple independent HTML tables  
3. Clean numeric values and handle missing data  
4. Merge datasets using left joins  
5. Export the final dataset as a CSV file  

## Output

The final dataset is saved as:

final_city_tourism_dataset.csv


## Author

Parisa Solouki Shahrezaie

