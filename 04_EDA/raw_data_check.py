import pandas as pd


# ============================================================
# CARS24 RAW DATA VALIDATION
# ============================================================

FILE_PATH = "02_Raw_Data/cars24_raw.csv"


print("=" * 70)
print("CARS24 RAW DATA VALIDATION")
print("=" * 70)


# ============================================================
# LOAD DATA
# ============================================================

print("\nLoading raw dataset...")

df = pd.read_csv(FILE_PATH)

print("Dataset loaded successfully!")


# ============================================================
# DATASET SIZE
# ============================================================

print("\n" + "=" * 70)
print("1. DATASET SIZE")
print("=" * 70)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")


# ============================================================
# COLUMN NAMES
# ============================================================

print("\n" + "=" * 70)
print("2. COLUMN NAMES")
print("=" * 70)

for i, column in enumerate(df.columns, start=1):

    print(f"{i:2}. {column}")


# ============================================================
# DATA TYPES
# ============================================================

print("\n" + "=" * 70)
print("3. DATA TYPES")
print("=" * 70)

print(df.dtypes)


# ============================================================
# MISSING VALUES
# ============================================================

print("\n" + "=" * 70)
print("4. MISSING VALUES")
print("=" * 70)

missing = df.isnull().sum()

missing_percentage = (
    df.isnull().mean() * 100
).round(2)


missing_report = pd.DataFrame({

    "Missing_Count": missing,

    "Missing_Percentage":
        missing_percentage

})


print(missing_report)


# ============================================================
# DUPLICATE RECORDS
# ============================================================

print("\n" + "=" * 70)
print("5. DUPLICATE RECORDS")
print("=" * 70)

duplicates = df.duplicated().sum()

print(
    f"Duplicate rows : {duplicates}"
)


# ============================================================
# UNIQUE VALUES
# ============================================================

print("\n" + "=" * 70)
print("6. UNIQUE VALUES")
print("=" * 70)

for column in df.columns:

    print(
        f"{column:25} : "
        f"{df[column].nunique()} unique values"
    )


# ============================================================
# SAMPLE DATA
# ============================================================

print("\n" + "=" * 70)
print("7. FIRST 5 RECORDS")
print("=" * 70)

print(
    df.head(5).to_string(index=False)
)


# ============================================================
# NUMERIC SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("8. NUMERIC DATA SUMMARY")
print("=" * 70)

print(
    df.describe().to_string()
)


# ============================================================
# CATEGORICAL SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("9. IMPORTANT CATEGORICAL VALUES")
print("=" * 70)


categorical_columns = [

    "make",
    "fuel_type",
    "transmission",
    "body_type",
    "ownership",
    "city_code"

]


for column in categorical_columns:

    if column in df.columns:

        print("\n" + "-" * 50)

        print(
            f"{column.upper()}"
        )

        print(
            df[column]
            .value_counts(dropna=False)
            .head(15)
        )


# ============================================================
# PRICE CHECK
# ============================================================

print("\n" + "=" * 70)
print("10. PRICE CHECK")
print("=" * 70)

if "listing_price" in df.columns:

    print(
        f"Minimum price : "
        f"{df['listing_price'].min()}"
    )

    print(
        f"Maximum price : "
        f"{df['listing_price'].max()}"
    )

    print(
        f"Average price : "
        f"{df['listing_price'].mean():.2f}"
    )


# ============================================================
# ODOMETER CHECK
# ============================================================

print("\n" + "=" * 70)
print("11. ODOMETER CHECK")
print("=" * 70)

if "odometer_km" in df.columns:

    print(
        f"Minimum km : "
        f"{df['odometer_km'].min()}"
    )

    print(
        f"Maximum km : "
        f"{df['odometer_km'].max()}"
    )

    print(
        f"Average km : "
        f"{df['odometer_km'].mean():.2f}"
    )


# ============================================================
# YEAR CHECK
# ============================================================

print("\n" + "=" * 70)
print("12. YEAR CHECK")
print("=" * 70)

if "year" in df.columns:

    print(
        f"Oldest car year : "
        f"{df['year'].min()}"
    )

    print(
        f"Newest car year : "
        f"{df['year'].max()}"
    )


# ============================================================
# END
# ============================================================

print("\n" + "=" * 70)
print("RAW DATA VALIDATION COMPLETED")
print("=" * 70)