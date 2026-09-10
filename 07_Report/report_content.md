# Cars24 Used Car Market Analysis

## 1. Executive Summary

This project analyzes used car listings collected from Cars24.

The project follows a complete data analytics workflow:

- Web scraping
- Raw data extraction
- Data cleaning
- Exploratory data analysis
- Data visualization
- Power BI dashboard development

Python was used for data collection, cleaning and analysis, while Power BI was used to create an interactive dashboard for business insights.

---

## 2. Business Problem

The used-car market contains vehicles with different brands, prices, manufacturing years, fuel types, transmission types and mileage levels.

The objective of this project is to analyze Cars24 used-car listings and understand:

- Car availability by brand
- Used-car price patterns
- Fuel type distribution
- Transmission preferences
- Manufacturing year distribution
- Mileage patterns
- Relationship between mileage and price
- Location-wise availability

---

## 3. Project Objectives

The main objectives are:

1. Collect used-car listing data.
2. Extract important vehicle attributes.
3. Clean and prepare the dataset.
4. Perform exploratory data analysis.
5. Identify important pricing and market patterns.
6. Build meaningful visualizations.
7. Develop an interactive Power BI dashboard.
8. Present business-oriented insights.

---

## 4. Data Collection

Cars24 used-car listing information was collected using Python and Selenium.

The scraped webpage was saved as an HTML file and the listing information was extracted from the webpage data.

The raw dataset was stored in:

`02_Raw_Data/cars24_raw.csv`

---

## 5. Data Cleaning

The raw dataset was processed using Python and Pandas.

The cleaning process included:

- Removing completely empty columns
- Cleaning text fields
- Removing unnecessary spaces
- Converting numerical fields to numeric data types
- Checking invalid prices
- Checking invalid mileage values
- Checking vehicle manufacturing years
- Removing duplicate listings
- Resetting the dataset index
- Creating the final cleaned dataset

The cleaned dataset was stored in:

`03_Cleaned_Data/cars24_cleaned.csv`

---

## 6. Exploratory Data Analysis

Exploratory data analysis was performed to understand the structure and characteristics of the dataset.

The analysis covered:

- Brand distribution
- Average price by brand
- Fuel type distribution
- Transmission distribution
- Body type distribution
- Manufacturing year
- Average price by manufacturing year
- Mileage statistics
- Mileage versus price
- Location distribution
- City distribution
- Ownership
- Highest-priced vehicles
- Lowest-priced vehicles

---

## 7. Data Visualizations

Python was used to create visualizations for the major analytical questions.

The project includes:

1. Cars by Brand
2. Average Used Car Price by Brand
3. Used Car Price Distribution
4. Fuel Type Distribution
5. Transmission Distribution
6. Cars by Manufacturing Year
7. Average Price by Manufacturing Year
8. Mileage versus Price

---

## 8. Power BI Dashboard

An interactive Power BI dashboard was developed using the cleaned Cars24 dataset.

The dashboard contains:

### Key Performance Indicators

- Total Cars
- Average Car Price
- Average Mileage
- Average Car Age

### Dashboard Visuals

- Cars by Brand
- Average Price by Brand
- Average Price by Manufacturing Year
- Fuel Type Distribution
- Transmission Distribution
- Mileage versus Price

### Interactive Filters

- Brand
- Fuel Type
- Transmission
- Manufacturing Year
- City

The dashboard allows users to filter the dataset and interactively analyze the used-car listings.

---

## 9. Key Insights

The analysis helps identify patterns in:

- Brand availability
- Used-car pricing
- Vehicle age
- Mileage
- Fuel type
- Transmission type
- Geographic availability

The detailed numerical findings are based on the scraped sample dataset used in this project.

---

## 10. Business Recommendations

Based on the analysis, used-car platforms can consider:

- Monitoring demand and inventory by brand.
- Comparing pricing across vehicle brands.
- Considering vehicle age and mileage when evaluating prices.
- Understanding customer preferences for fuel and transmission types.
- Using location-level inventory information to improve vehicle allocation.
- Using interactive dashboards for faster inventory and pricing analysis.

---

## 11. Tools and Technologies

### Programming

- Python
- Pandas
- NumPy

### Web Scraping

- Selenium
- BeautifulSoup
- HTML

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Business Intelligence

- Microsoft Power BI

### Development Environment

- Visual Studio Code

---

## 12. Project Structure

```text
Cars24_Used_Car_Analysis/

├── 01_Web_Scraping/
├── 02_Raw_Data/
├── 03_Cleaned_Data/
├── 04_EDA/
├── 05_Visualizations/
├── 06_PowerBI/
├── 07_Report/
├── 08_Presentation/
├── main.py
├── README.md
└── requirements.txt