# login_pinterest.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from utils import load_cookies
import os
import time

def login_and_save_cookies(return_driver=False):
    options = webdriver.FirefoxOptions()
    options.add_argument("--width=1280")
    options.add_argument("--height=800")

    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 20)

    # Step 1: Visit Pinterest FIRST before loading cookies
    print("🌐 Visiting Pinterest homepage...")
    driver.get("https://www.pinterest.com/")
    time.sleep(2)

    cookie_file = "cookies_magicmushroomshop_account.json"
    if os.path.exists(cookie_file):
        print("🍪 Loading cookies...")
        load_cookies(driver, cookie_file)

        # Step 2: Reload the page after cookies are added
        print("🔄 Refreshing page after loading cookies...")
        driver.get("https://www.pinterest.com/")
    else:
        print("❌ Cookie file not found. Run savecookies.py first.")
        driver.quit()
        return None, None

    return driver, wait