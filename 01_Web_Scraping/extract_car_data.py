import re
import csv
import os


# ============================================================
# CARS24 CAR DATA EXTRACTION
# ============================================================

HTML_FILE = "02_Raw_Data/cars24_page.html"
CSV_FILE = "02_Raw_Data/cars24_raw.csv"


# ============================================================
# START
# ============================================================

print("=" * 70)
print("CARS24 DATA EXTRACTION")
print("=" * 70)


# ============================================================
# READ HTML FILE
# ============================================================

print()
print("Reading Cars24 HTML file...")

try:

    with open(
        HTML_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        html = file.read()

except FileNotFoundError:

    print()
    print("ERROR: HTML file not found!")
    print(f"Expected file: {HTML_FILE}")
    exit()


print("HTML loaded successfully!")
print(f"HTML size: {len(html):,} characters")


# ============================================================
# FIND LISTING OBJECTS
# ============================================================

print()
print("Searching for Cars24 listing records...")


# Every car listing starts with appointmentId.
#
# Example:
#
# {\"appointmentId\":\"11623979176\",\"bodyType\":\"Hatchback\"
#
# We split the page using this structure.


listing_pattern = (
    r'\{\\"appointmentId\\":\\".*?'
    r'(?=\{\\"appointmentId\\":\\"|$)'
)


matches = re.findall(
    listing_pattern,
    html,
    flags=re.DOTALL
)


print(
    f"Potential listing records found: {len(matches)}"
)


# ============================================================
# BACKUP LISTING EXTRACTION
# ============================================================

if len(matches) == 0:

    print()
    print("Primary extraction failed.")
    print("Trying backup extraction...")


    positions = [
        match.start()
        for match in re.finditer(
            r'\{\\"appointmentId\\":\\"',
            html
        )
    ]


    print(
        f"Listing starting positions found: {len(positions)}"
    )


    for index, start in enumerate(positions):

        if index + 1 < len(positions):

            end = positions[index + 1]

        else:

            end = len(html)


        matches.append(
            html[start:end]
        )


# ============================================================
# HELPER FUNCTION
# ============================================================

def extract_string(text, field):

    pattern = (
        r'\\"'
        + re.escape(field)
        + r'\\":\\"(.*?)\\"'
    )

    match = re.search(
        pattern,
        text,
        flags=re.DOTALL
    )

    if match:

        return match.group(1)

    return ""


# ============================================================
# NUMERIC FIELD
# ============================================================

def extract_number(text, field):

    pattern = (
        r'\\"'
        + re.escape(field)
        + r'\\":(\d+(?:\.\d+)?)'
    )

    match = re.search(
        pattern,
        text
    )

    if match:

        return match.group(1)

    return ""


# ============================================================
# NESTED NUMERIC FIELD
# ============================================================

def extract_nested_number(
    text,
    parent,
    child
):

    pattern = (
        r'\\"'
        + re.escape(parent)
        + r'\\":\{'
        + r'\\"'
        + re.escape(child)
        + r'\\":(\d+)'
    )

    match = re.search(
        pattern,
        text
    )

    if match:

        return match.group(1)

    return ""


# ============================================================
# NESTED STRING FIELD
# ============================================================

def extract_nested_string(
    text,
    parent,
    child
):

    pattern = (
        r'\\"'
        + re.escape(parent)
        + r'\\":\{'
        + r'.*?'
        + r'\\"'
        + re.escape(child)
        + r'\\":\\"(.*?)\\"'
    )

    match = re.search(
        pattern,
        text,
        flags=re.DOTALL
    )

    if match:

        return match.group(1)

    return ""


# ============================================================
# CLEAN TEXT
# ============================================================

def clean_text(value):

    if value is None:

        return ""

    value = value.replace(
        "\\\\n",
        " "
    )

    value = value.replace(
        "\\n",
        " "
    )

    value = value.replace(
        "\\\\",
        ""
    )

    return value.strip()


# ============================================================
# EXTRACT CAR RECORDS
# ============================================================

print()
print("Extracting car information...")


cars = []


for listing in matches:

    # --------------------------------------------------------
    # BASIC IDENTIFICATION
    # --------------------------------------------------------

    appointment_id = extract_string(
        listing,
        "appointmentId"
    )

    car_name = extract_string(
        listing,
        "carName"
    )

    make = extract_string(
        listing,
        "make"
    )

    model = extract_string(
        listing,
        "model"
    )

    body_type = extract_string(
        listing,
        "bodyType"
    )

    fuel_type = extract_string(
        listing,
        "fuelType"
    )

    variant = extract_string(
        listing,
        "variant"
    )

    masked_reg_num = extract_string(
        listing,
        "maskedRegNum"
    )

    city_code = extract_string(
        listing,
        "cityCode"
    )

    city_rto = extract_string(
        listing,
        "cityRto"
    )

    status = extract_string(
        listing,
        "status"
    )

    business_vertical = extract_string(
        listing,
        "businessVertical"
    )

    car_segment = extract_string(
        listing,
        "carSegment"
    )


    # --------------------------------------------------------
    # NUMERIC FIELDS
    # --------------------------------------------------------

    year = extract_number(
        listing,
        "year"
    )

    listing_price = extract_number(
        listing,
        "listingPrice"
    )

    original_price = extract_number(
        listing,
        "originalPrice"
    )

    discount = extract_number(
        listing,
        "discount"
    )

    ownership = extract_number(
        listing,
        "ownership"
    )

    location_id = extract_number(
        listing,
        "locationId"
    )


    # --------------------------------------------------------
    # IMPORTANT:
    # ODOMETER IS A NESTED NUMERIC VALUE
    #
    # "odometer":{"value":65347,"display":"65,347 km"}
    # --------------------------------------------------------

    odometer_km = extract_nested_number(
        listing,
        "odometer",
        "value"
    )


    # --------------------------------------------------------
    # TRANSMISSION IS A NESTED STRING VALUE
    #
    # "transmissionType":{"value":"Automatic","display":"Auto"}
    # --------------------------------------------------------

    transmission = extract_nested_string(
        listing,
        "transmissionType",
        "value"
    )


    # --------------------------------------------------------
    # LOCATION
    #
    # "address":{"locality":"Kakkanad, Kochi", ...}
    # --------------------------------------------------------

    location = extract_nested_string(
        listing,
        "address",
        "locality"
    )


    # --------------------------------------------------------
    # CLEAN TEXT VALUES
    # --------------------------------------------------------

    car_name = clean_text(car_name)

    make = clean_text(make)

    model = clean_text(model)

    body_type = clean_text(body_type)

    fuel_type = clean_text(fuel_type)

    transmission = clean_text(transmission)

    variant = clean_text(variant)

    masked_reg_num = clean_text(masked_reg_num)

    city_code = clean_text(city_code)

    city_rto = clean_text(city_rto)

    location = clean_text(location)

    status = clean_text(status)

    business_vertical = clean_text(
        business_vertical
    )

    car_segment = clean_text(
        car_segment
    )


    # --------------------------------------------------------
    # KEEP ONLY VALID CAR RECORDS
    # --------------------------------------------------------

    if (
        appointment_id != ""
        and car_name != ""
        and listing_price != ""
    ):

        car = {

            "appointment_id":
                appointment_id,

            "car_name":
                car_name,

            "make":
                make,

            "model":
                model,

            "body_type":
                body_type,

            "fuel_type":
                fuel_type,

            "transmission":
                transmission,

            "variant":
                variant,

            "year":
                year,

            "listing_price":
                listing_price,

            "original_price":
                original_price,

            "discount":
                discount,

            "odometer_km":
                odometer_km,

            "ownership":
                ownership,

            "location":
                location,

            "city_code":
                city_code,

            "city_rto":
                city_rto,

            "location_id":
                location_id,

            "registration_number":
                masked_reg_num,

            "status":
                status,

            "business_vertical":
                business_vertical,

            "car_segment":
                car_segment

        }

        cars.append(
            car
        )


# ============================================================
# REMOVE DUPLICATES
# ============================================================

print()
print("Removing duplicate listings...")


unique_cars = []

seen_ids = set()


for car in cars:

    appointment_id = car[
        "appointment_id"
    ]

    if appointment_id not in seen_ids:

        seen_ids.add(
            appointment_id
        )

        unique_cars.append(
            car
        )


cars = unique_cars


# ============================================================
# CSV COLUMNS
# ============================================================

fieldnames = [

    "appointment_id",

    "car_name",

    "make",

    "model",

    "body_type",

    "fuel_type",

    "transmission",

    "variant",

    "year",

    "listing_price",

    "original_price",

    "discount",

    "odometer_km",

    "ownership",

    "location",

    "city_code",

    "city_rto",

    "location_id",

    "registration_number",

    "status",

    "business_vertical",

    "car_segment"

]


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

os.makedirs(
    "02_Raw_Data",
    exist_ok=True
)


# ============================================================
# SAVE CSV
# ============================================================

print()
print("Saving data to CSV...")


with open(
    CSV_FILE,
    "w",
    newline="",
    encoding="utf-8-sig"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(
        cars
    )


# ============================================================
# FINAL RESULTS
# ============================================================

print()
print("=" * 70)
print("DATA EXTRACTION COMPLETED")
print("=" * 70)

print()

print(
    f"Listing objects found : {len(matches)}"
)

print(
    f"Valid car records     : {len(cars)}"
)

print(
    f"CSV file              : {CSV_FILE}"
)


# ============================================================
# DISPLAY SAMPLE RECORDS
# ============================================================

print()
print("First 5 extracted cars:")
print("-" * 70)


for index, car in enumerate(
    cars[:5],
    start=1
):

    print()

    print(
        f"Car {index}"
    )

    print(
        f"  Name         : "
        f"{car['car_name']}"
    )

    print(
        f"  Make         : "
        f"{car['make']}"
    )

    print(
        f"  Model        : "
        f"{car['model']}"
    )

    print(
        f"  Year         : "
        f"{car['year']}"
    )

    print(
        f"  Fuel         : "
        f"{car['fuel_type']}"
    )

    print(
        f"  Transmission : "
        f"{car['transmission']}"
    )

    print(
        f"  Variant      : "
        f"{car['variant']}"
    )

    print(
        f"  Price        : "
        f"{car['listing_price']}"
    )

    print(
        f"  Odometer     : "
        f"{car['odometer_km']} km"
    )

    print(
        f"  Location     : "
        f"{car['location']}"
    )


print()
print("=" * 70)
print("DONE")
print("=" * 70)