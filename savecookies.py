# savecookies.py

import json
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os

# Make sure cookies are saved as JSON, not pickle
cookie_filename = os.path.join(os.path.dirname(__file__), "cookies_magicmushroomshop_account.json")

options = Options()
options.add_argument("--width=1280")
options.add_argument("--height=800")

driver = webdriver.Firefox(options=options)

# Open Pinterest
driver.get("https://www.pinterest.com/")
print("🔐 Please log in manually in the browser window... You have 60 seconds.")
time.sleep(60)  # ⏳ Wait while user logs in manually

# Save cookies as JSON
cookies = driver.get_cookies()
with open(cookie_filename, "w") as f:
    json.dump(cookies, f)

print(f"✅ Cookies saved to {cookie_filename}")
driver.quit()
