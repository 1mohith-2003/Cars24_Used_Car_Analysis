from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os


def scrape_cars24():

    # Cars24 used cars page
    url = "https://www.cars24.com/buy-used-car/"

    # Chrome settings
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # Start Chrome
    print("Starting Chrome...")
    driver = webdriver.Chrome(options=options)

    try:

        # Open Cars24 used cars page
        print("Opening Cars24 used cars page...")
        driver.get(url)

        # Wait for page to load
        time.sleep(8)

        print("Page loaded successfully!")

        # Scroll down to load more cars
        print("Scrolling page to load car listings...")

        for i in range(10):

            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            time.sleep(2)

            print(f"Scroll {i + 1}/10 completed")

        # Get complete HTML
        html = driver.page_source

        # Create output folder if it doesn't exist
        output_folder = "02_Raw_Data"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Save HTML
        output_file = os.path.join(
            output_folder,
            "cars24_page.html"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(html)

        # Display results
        print()
        print("=" * 60)
        print("SCRAPING COMPLETED")
        print("=" * 60)

        print(f"URL: {url}")
        print(f"HTML size: {len(html):,} characters")
        print(f"Saved file: {output_file}")

    except Exception as e:

        print()
        print("=" * 60)
        print("ERROR OCCURRED")
        print("=" * 60)

        print(e)

    finally:

        # Close browser
        print()
        print("Closing Chrome...")
        driver.quit()


if __name__ == "__main__":
    scrape_cars24()