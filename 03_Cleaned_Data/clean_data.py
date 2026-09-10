import pandas as pd
import os


# ============================================================
# CARS24 DATA CLEANING
# ============================================================

RAW_FILE = "02_Raw_Data/cars24_raw.csv"
CLEAN_FILE = "03_Cleaned_Data/cars24_cleaned.csv"


print("=" * 70)
print("CARS24 DATA CLEANING")
print("=" * 70)


# ============================================================
# 1. LOAD RAW DATA
# ============================================================

print("\nLoading raw dataset...")

df = pd.read_csv(
    RAW_FILE,
    encoding="utf-8-sig"
)

print("Raw dataset loaded successfully!")

print(
    f"Original rows    : {df.shape[0]}"
)

print(
    f"Original columns : {df.shape[1]}"
)


# ============================================================
# 2. REMOVE COMPLETELY EMPTY COLUMNS
# ============================================================

print("\nChecking completely empty columns...")

empty_columns = [
    column
    for column in df.columns
    if df[column].isna().all()
]

if empty_columns:

    print(
        "Removing empty columns:",
        empty_columns
    )

    df.drop(
        columns=empty_columns,
        inplace=True
    )

else:

    print("No completely empty columns found.")


# ============================================================
# 3. CLEAN TEXT COLUMNS
# ============================================================

print("\nCleaning text columns...")


text_columns = [

    "appointment_id",
    "car_name",
    "make",
    "model",
    "body_type",
    "fuel_type",
    "transmission",
    "variant",
    "location",
    "city_code",
    "city_rto",
    "registration_number",
    "status",
    "business_vertical",
    "car_segment"

]


for column in text_columns:

    if column in df.columns:

        df[column] = (
            df[column]
            .astype("string")
            .str.strip()
        )

        # Replace multiple spaces
        df[column] = (
            df[column]
            .str.replace(
                r"\s+",
                " ",
                regex=True
            )
        )


# ============================================================
# 4. CONVERT NUMERIC COLUMNS
# ============================================================

print("\nConverting numeric columns...")


numeric_columns = [

    "year",
    "listing_price",
    "original_price",
    "discount",
    "odometer_km",
    "ownership",
    "location_id"

]


for column in numeric_columns:

    if column in df.columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )


# ============================================================
# 5. STANDARDIZE CATEGORICAL VALUES
# ============================================================

print("\nStandardizing categorical values...")


if "fuel_type" in df.columns:

    df["fuel_type"] = (
        df["fuel_type"]
        .str.title()
    )


if "transmission" in df.columns:

    df["transmission"] = (
        df["transmission"]
        .str.title()
    )


if "body_type" in df.columns:

    df["body_type"] = (
        df["body_type"]
        .str.title()
    )


if "make" in df.columns:

    df["make"] = (
        df["make"]
        .str.title()
    )


# ============================================================
# 6. HANDLE INVALID PRICES
# ============================================================

print("\nChecking invalid prices...")


if "listing_price" in df.columns:

    invalid_price = (
        df["listing_price"] <= 0
    )

    print(
        f"Invalid price records : "
        f"{invalid_price.sum()}"
    )

    df.loc[
        invalid_price,
        "listing_price"
    ] = pd.NA


# ============================================================
# 7. HANDLE INVALID ODOMETER VALUES
# ============================================================

print("\nChecking invalid odometer values...")


if "odometer_km" in df.columns:

    invalid_odometer = (
        df["odometer_km"] < 0
    )

    print(
        f"Invalid odometer records : "
        f"{invalid_odometer.sum()}"
    )

    df.loc[
        invalid_odometer,
        "odometer_km"
    ] = pd.NA


# ============================================================
# 8. CHECK CAR YEAR
# ============================================================

print("\nChecking car manufacturing years...")


if "year" in df.columns:

    invalid_year = (
        (df["year"] < 1990)
        |
        (df["year"] > 2026)
    )

    print(
        f"Invalid year records : "
        f"{invalid_year.sum()}"
    )

    df.loc[
        invalid_year,
        "year"
    ] = pd.NA


# ============================================================
# 9. REMOVE DUPLICATE APPOINTMENT IDs
# ============================================================

print("\nChecking duplicate listings...")


if "appointment_id" in df.columns:

    before_duplicates = len(df)

    df = df.drop_duplicates(
        subset="appointment_id",
        keep="first"
    )

    removed_duplicates = (
        before_duplicates - len(df)
    )

    print(
        f"Duplicate listings removed : "
        f"{removed_duplicates}"
    )


# ============================================================
# 10. CHECK MISSING VALUES
# ============================================================

print("\nMissing values after cleaning:")

missing = df.isna().sum()

missing = missing[
    missing > 0
]

if len(missing) == 0:

    print("No missing values found.")

else:

    print(missing)


# ============================================================
# 11. SORT DATA
# ============================================================

print("\nSorting dataset...")


if "listing_price" in df.columns:

    df = df.sort_values(
        by="listing_price",
        ascending=False
    )


# ============================================================
# 12. RESET INDEX
# ============================================================

df = df.reset_index(
    drop=True
)


# ============================================================
# 13. CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(
    "03_Cleaned_Data",
    exist_ok=True
)


# ============================================================
# 14. SAVE CLEANED DATA
# ============================================================

print("\nSaving cleaned dataset...")


df.to_csv(
    CLEAN_FILE,
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 15. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED")
print("=" * 70)

print()

print(
    f"Rows before cleaning : "
    f"{before_duplicates if 'before_duplicates' in locals() else 'N/A'}"
)

print(
    f"Rows after cleaning  : "
    f"{len(df)}"
)

print(
    f"Columns              : "
    f"{len(df.columns)}"
)

print(
    f"Output file          : "
    f"{CLEAN_FILE}"
)


# ============================================================
# 16. DISPLAY SAMPLE
# ============================================================

print("\nFirst 5 cleaned records:")
print("-" * 70)

print(
    df.head(5).to_string(
        index=False
    )
)


print("\n" + "=" * 70)
print("DONE")
print("=" * 70)