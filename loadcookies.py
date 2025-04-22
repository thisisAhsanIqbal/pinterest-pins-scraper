# savecookies.py

import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import EMAIL, PASSWORD

cookie_filename = os.path.join(os.path.dirname(__file__), "cookies_magicmushroomshop_account.json")

options = Options()
options.add_argument("--width=1280")
options.add_argument("--height=800")

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 20)

driver.get("https://www.pinterest.com/")
print("🌐 Pinterest loaded")

# Click login button
login_btn_xpath = "//div[text()='Log in' and contains(@class, 'tBJ') and contains(@class, 'dyH')]"
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, login_btn_xpath)))
login_btn.click()

# Fill login form
email_input = wait.until(EC.presence_of_element_located((By.NAME, "id")))
password_input = driver.find_element(By.NAME, "password")
email_input.send_keys(EMAIL)
password_input.send_keys(PASSWORD)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Wait for login to complete
try:
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='simple-user-avatar']")))
    print("✅ Logged in successfully!")
except:
    print("⚠️ Login might have failed. Screenshot saved.")
    driver.save_screenshot("login_fail.png")

# Save cookies
cookies = driver.get_cookies()
with open(cookie_filename, "w") as f:
    json.dump(cookies, f)

print(f"✅ Cookies saved to {cookie_filename}")
driver.quit()
