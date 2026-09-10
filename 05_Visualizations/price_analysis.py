import pandas as pd
import matplotlib.pyplot as plt
import os


# ============================================================
# CARS24 PRICE ANALYSIS
# ============================================================

INPUT_FILE = "03_Cleaned_Data/cars24_cleaned.csv"
OUTPUT_FOLDER = "05_Visualizations/visualizations"


print("=" * 70)
print("CARS24 PRICE & MARKET VISUALIZATION")
print("=" * 70)


# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(
    INPUT_FILE,
    encoding="utf-8-sig"
)


os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


# ============================================================
# 1. PRICE DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.hist(
    df["listing_price"],
    bins=10
)

plt.title(
    "Distribution of Used Car Prices"
)

plt.xlabel(
    "Listing Price (₹)"
)

plt.ylabel(
    "Number of Cars"
)

plt.ticklabel_format(
    style="plain",
    axis="x"
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/03_price_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 2. FUEL TYPE DISTRIBUTION
# ============================================================

fuel_counts = (
    df["fuel_type"]
    .value_counts()
)


plt.figure(
    figsize=(8, 6)
)

fuel_counts.plot(
    kind="bar"
)

plt.title(
    "Cars by Fuel Type"
)

plt.xlabel(
    "Fuel Type"
)

plt.ylabel(
    "Number of Cars"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/04_fuel_type_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 3. TRANSMISSION DISTRIBUTION
# ============================================================

transmission_counts = (
    df["transmission"]
    .value_counts()
)


plt.figure(
    figsize=(8, 6)
)

transmission_counts.plot(
    kind="bar"
)

plt.title(
    "Cars by Transmission Type"
)

plt.xlabel(
    "Transmission"
)

plt.ylabel(
    "Number of Cars"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/05_transmission_distribution.png",
    dpi=300
)

plt.close()


# ============================================================
# 4. CARS BY YEAR
# ============================================================

year_counts = (
    df["year"]
    .value_counts()
    .sort_index()
)


plt.figure(
    figsize=(10, 6)
)

year_counts.plot(
    kind="bar"
)

plt.title(
    "Number of Cars by Manufacturing Year"
)

plt.xlabel(
    "Manufacturing Year"
)

plt.ylabel(
    "Number of Cars"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/06_cars_by_year.png",
    dpi=300
)

plt.close()


# ============================================================
# 5. YEAR VS AVERAGE PRICE
# ============================================================

year_price = (
    df.groupby("year")["listing_price"]
    .mean()
    .sort_index()
)


plt.figure(
    figsize=(10, 6)
)

plt.plot(
    year_price.index,
    year_price.values,
    marker="o"
)

plt.title(
    "Average Used Car Price by Manufacturing Year"
)

plt.xlabel(
    "Manufacturing Year"
)

plt.ylabel(
    "Average Listing Price (₹)"
)

plt.ticklabel_format(
    style="plain",
    axis="y"
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/07_year_vs_average_price.png",
    dpi=300
)

plt.close()


# ============================================================
# 6. MILEAGE VS PRICE
# ============================================================

plt.figure(
    figsize=(10, 6)
)

plt.scatter(
    df["odometer_km"],
    df["listing_price"]
)

plt.title(
    "Mileage vs Used Car Price"
)

plt.xlabel(
    "Mileage (km)"
)

plt.ylabel(
    "Listing Price (₹)"
)

plt.ticklabel_format(
    style="plain",
    axis="both"
)

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/08_mileage_vs_price.png",
    dpi=300
)

plt.close()


print("\nPrice and market visualizations created successfully!")

print(
    f"Saved in: {OUTPUT_FOLDER}"
)


print("\n" + "=" * 70)
print("DONE")
print("=" * 70)