# search_keywords.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scroll_pin_page import scroll_for_pins

def search_keywords(driver, wait):
    time.sleep(2)  # Allow page to settle

    # Click the search icon to open the search bar
    search_icon_xpath = "//button[@aria-label='Search icon']"
    search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, search_icon_xpath)))
    search_icon.click()

    # Load keywords from file
    try:
        with open("kw.txt", "r", encoding="utf-8") as f:
            keywords = [kw.strip() for kw in f.readlines() if kw.strip()]
    except FileNotFoundError:
        print("❌ kw.txt not found!")
        return

    # Loop through each keyword and perform search
    for keyword in keywords:
        print(f"🔍 Searching: {keyword}")

        # Find search input and send keyword
        search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-test-id='search-box-input']")))
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)

        # Wait for results to load
        time.sleep(3)

        # Scroll to load pins
        
        scroll_for_pins(driver, max_scrolls=20, output_file="pin_urls.txt")


        # Optional delay before next search
        time.sleep(2)
