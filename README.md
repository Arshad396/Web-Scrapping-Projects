# 🕸️ Web Scraping Projects ✨

This repository contains two robust Python-based web scraping scripts that extract high-value data from dynamic websites using Selenium and Pandas. Ideal for real-world data analysis and automation enthusiasts.

## 1. 🏡 99Acres Property Scraper (Chennai)
Filename: 01.properties-scraper.py
Description:
This script scrapes detailed property listings from 99acres.com (focused on Chennai). It uses Selenium to interact with dynamic web content and pandas to structure the extracted data. The final dataset is saved in an Excel file: chennai-properties-99acres.xlsx.

🔑 Key Features:

Automates search and navigation across property listings.

Applies filters: ✅ Verified, 🏗️ Ready To Move, 🖼️ With Photos, 🎥 With Videos.

Extracts property name, location, price, area, and BHK configuration.

Handles pagination to gather listings from multiple pages.

Cleans and formats the data using pandas.

Exports the final dataset to Excel.

## 📦 Libraries Used:
selenium, pandas

⚠️ Note: The site is dynamically loaded—expect longer wait times due to explicit Selenium waits.

## 2. 📈 Yahoo Finance Stock Scraper
Filename: 01.stocks-scraper.py
Description:
This script targets the "Most Active" stocks listed on Yahoo Finance. It scrapes vital stock metrics such as symbol, price, change, volume, market cap, and P/E ratio. The structured output is saved to yahoo-stocks-data.xlsx.

## 🔑 Key Features:

Automates browsing of Yahoo Finance’s "Most Active" stocks section.

Extracts stock name, symbol, price, change %, volume, market cap, and P/E ratio.

Navigates and scrapes data across multiple pages.

Structures and cleans the data using pandas.

Exports to a neatly formatted Excel sheet.

## 📦 Libraries Used:
selenium, pandas

✅ Requirements
Ensure the following Python packages are installed:

bash
Copy
Edit
pip install selenium pandas
Also, download the appropriate ChromeDriver matching your Chrome version and place it in your system path.

## 📂 Output Files
chennai-properties-99acres.xlsx

yahoo-stocks-data.xlsx

## 🤖 Usage
Run the scripts using Python 3:

bash
Copy
Edit
python 01.properties-scraper.py
python 01.stocks-scraper.py
📌 Disclaimer
These scripts are for educational and research purposes only. Be mindful of each website’s robots.txt and scraping policies.
