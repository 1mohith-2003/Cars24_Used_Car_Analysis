import pandas as pd
import matplotlib.pyplot as plt
import os


# ============================================================
# CARS24 BRAND ANALYSIS
# ============================================================

INPUT_FILE = "03_Cleaned_Data/cars24_cleaned.csv"
OUTPUT_FOLDER = "05_Visualizations/visualizations"


print("=" * 70)
print("CARS24 BRAND VISUALIZATION")
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
# 1. CAR LISTINGS BY BRAND
# ============================================================

brand_counts = (
    df["make"]
    .value_counts()
    .head(10)
)


plt.figure(
    figsize=(10, 6)
)

brand_counts.sort_values().plot(
    kind="barh"
)

plt.title(
    "Top Car Brands by Number of Listings"
)

plt.xlabel(
    "Number of Listings"
)

plt.ylabel(
    "Car Brand"
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/01_brand_listings.png",
    dpi=300
)

plt.close()


# ============================================================
# 2. AVERAGE PRICE BY BRAND
# ============================================================

brand_price = (
    df.groupby("make")["listing_price"]
    .mean()
    .sort_values(
        ascending=False
    )
    .head(10)
)


plt.figure(
    figsize=(10, 6)
)

brand_price.sort_values().plot(
    kind="barh"
)

plt.title(
    "Average Used Car Price by Brand"
)

plt.xlabel(
    "Average Price (₹)"
)

plt.ylabel(
    "Car Brand"
)

plt.ticklabel_format(
    style="plain",
    axis="x"
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/02_average_price_by_brand.png",
    dpi=300
)

plt.close()


print("\nBrand visualizations created successfully!")

print(
    f"Saved in: {OUTPUT_FOLDER}"
)


print("\n" + "=" * 70)
print("DONE")
print("=" * 70)