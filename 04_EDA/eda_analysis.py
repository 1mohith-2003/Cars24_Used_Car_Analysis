import pandas as pd
import os


# ============================================================
# CARS24 EXPLORATORY DATA ANALYSIS
# ============================================================

INPUT_FILE = "03_Cleaned_Data/cars24_cleaned.csv"
OUTPUT_FOLDER = "04_EDA"


print("=" * 70)
print("CARS24 USED CAR - EXPLORATORY DATA ANALYSIS")
print("=" * 70)


# ============================================================
# 1. LOAD DATA
# ============================================================

print("\nLoading cleaned dataset...")

df = pd.read_csv(
    INPUT_FILE,
    encoding="utf-8-sig"
)

print("Dataset loaded successfully!")

print(
    f"Rows    : {df.shape[0]}"
)

print(
    f"Columns : {df.shape[1]}"
)


# ============================================================
# 2. BASIC INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("1. BASIC DATASET INFORMATION")
print("=" * 70)

print(
    df.info()
)


# ============================================================
# 3. STATISTICAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("2. STATISTICAL SUMMARY")
print("=" * 70)

print(
    df.describe().to_string()
)


# ============================================================
# 4. BRAND ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("3. BRAND ANALYSIS")
print("=" * 70)


brand_counts = (
    df["make"]
    .value_counts()
)


print("\nNumber of cars by brand:")

print(
    brand_counts.to_string()
)


# ============================================================
# 5. BRAND PRICE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("4. AVERAGE PRICE BY BRAND")
print("=" * 70)


brand_price = (
    df.groupby("make")["listing_price"]
    .agg(
        ["count", "mean", "min", "max"]
    )
    .sort_values(
        "mean",
        ascending=False
    )
)


print(
    brand_price.to_string()
)


# ============================================================
# 6. FUEL TYPE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("5. FUEL TYPE ANALYSIS")
print("=" * 70)


fuel_analysis = (
    df["fuel_type"]
    .value_counts()
)


print(
    fuel_analysis.to_string()
)


# ============================================================
# 7. TRANSMISSION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("6. TRANSMISSION ANALYSIS")
print("=" * 70)


transmission_analysis = (
    df["transmission"]
    .value_counts()
)


print(
    transmission_analysis.to_string()
)


# ============================================================
# 8. BODY TYPE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("7. BODY TYPE ANALYSIS")
print("=" * 70)


body_type_analysis = (
    df["body_type"]
    .value_counts()
)


print(
    body_type_analysis.to_string()
)


# ============================================================
# 9. YEAR ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("8. CAR YEAR ANALYSIS")
print("=" * 70)


year_analysis = (
    df["year"]
    .value_counts()
    .sort_index(
        ascending=False
    )
)


print(
    year_analysis.to_string()
)


# ============================================================
# 10. AVERAGE PRICE BY YEAR
# ============================================================

print("\n" + "=" * 70)
print("9. AVERAGE PRICE BY CAR YEAR")
print("=" * 70)


year_price = (
    df.groupby("year")["listing_price"]
    .agg(
        ["count", "mean", "min", "max"]
    )
    .sort_index(
        ascending=False
    )
)


print(
    year_price.to_string()
)


# ============================================================
# 11. ODOMETER ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("10. ODOMETER ANALYSIS")
print("=" * 70)


print(
    f"Average mileage : "
    f"{df['odometer_km'].mean():,.0f} km"
)

print(
    f"Minimum mileage : "
    f"{df['odometer_km'].min():,.0f} km"
)

print(
    f"Maximum mileage : "
    f"{df['odometer_km'].max():,.0f} km"
)


# ============================================================
# 12. MILEAGE VS PRICE
# ============================================================

print("\n" + "=" * 70)
print("11. MILEAGE VS PRICE")
print("=" * 70)


correlation = (
    df[
        [
            "odometer_km",
            "listing_price"
        ]
    ]
    .corr()
)


print(
    correlation.to_string()
)


# ============================================================
# 13. LOCATION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("12. TOP LOCATIONS")
print("=" * 70)


location_analysis = (
    df["location"]
    .value_counts()
    .head(15)
)


print(
    location_analysis.to_string()
)


# ============================================================
# 14. CITY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("13. CITY ANALYSIS")
print("=" * 70)


if "city_code" in df.columns:

    city_analysis = (
        df["city_code"]
        .value_counts()
    )

    print(
        city_analysis.to_string()
    )


# ============================================================
# 15. OWNERSHIP ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("14. OWNERSHIP ANALYSIS")
print("=" * 70)


if "ownership" in df.columns:

    ownership_analysis = (
        df["ownership"]
        .value_counts()
        .sort_index()
    )

    print(
        ownership_analysis.to_string()
    )


# ============================================================
# 16. PRICE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("15. PRICE ANALYSIS")
print("=" * 70)


print(
    f"Average price : "
    f"₹{df['listing_price'].mean():,.0f}"
)

print(
    f"Median price  : "
    f"₹{df['listing_price'].median():,.0f}"
)

print(
    f"Minimum price : "
    f"₹{df['listing_price'].min():,.0f}"
)

print(
    f"Maximum price : "
    f"₹{df['listing_price'].max():,.0f}"
)


# ============================================================
# 17. TOP 10 MOST EXPENSIVE CARS
# ============================================================

print("\n" + "=" * 70)
print("16. TOP 10 MOST EXPENSIVE CARS")
print("=" * 70)


expensive_cars = (
    df[
        [
            "car_name",
            "make",
            "year",
            "listing_price",
            "odometer_km",
            "location"
        ]
    ]
    .sort_values(
        "listing_price",
        ascending=False
    )
    .head(10)
)


print(
    expensive_cars.to_string(
        index=False
    )
)


# ============================================================
# 18. TOP 10 LOWEST PRICED CARS
# ============================================================

print("\n" + "=" * 70)
print("17. TOP 10 LOWEST PRICED CARS")
print("=" * 70)


cheapest_cars = (
    df[
        [
            "car_name",
            "make",
            "year",
            "listing_price",
            "odometer_km",
            "location"
        ]
    ]
    .sort_values(
        "listing_price",
        ascending=True
    )
    .head(10)
)


print(
    cheapest_cars.to_string(
        index=False
    )
)


# ============================================================
# 19. SAVE EDA TABLES
# ============================================================

print("\n" + "=" * 70)
print("18. SAVING EDA RESULTS")
print("=" * 70)


os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


brand_price.to_csv(
    "04_EDA/brand_price_analysis.csv"
)

fuel_analysis.to_csv(
    "04_EDA/fuel_type_analysis.csv"
)

transmission_analysis.to_csv(
    "04_EDA/transmission_analysis.csv"
)

body_type_analysis.to_csv(
    "04_EDA/body_type_analysis.csv"
)

year_price.to_csv(
    "04_EDA/year_price_analysis.csv"
)

location_analysis.to_csv(
    "04_EDA/location_analysis.csv"
)


print(
    "EDA analysis files saved successfully!"
)


# ============================================================
# FINAL
# ============================================================

print("\n" + "=" * 70)
print("EDA ANALYSIS COMPLETED")
print("=" * 70)