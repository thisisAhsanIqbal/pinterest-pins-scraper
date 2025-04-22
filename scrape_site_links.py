# scrape_site_links.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scrape_site_links(driver, wait):
    print("🔗 Starting to scrape external site links from pins...")

    site_links = []
    action = ActionChains(driver)

    # Get all pin cards (these must be in DOM after scroll)
    pin_cards = driver.find_elements(By.XPATH, "//div[@data-test-id='pin']")

    print(f"📦 Found {len(pin_cards)} pins to inspect...")

    for idx, card in enumerate(pin_cards):
        try:
            # Scroll element into view
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
            time.sleep(0.3)

            # Hover to trigger "Visit site" button
            action.move_to_element(card).perform()
            time.sleep(0.6)  # Give time for hover popup to appear

            # Try to find visit-site button inside this pin
            visit_button = card.find_element(By.XPATH, ".//a[@data-test-id='visit-button']")
            site_url = visit_button.get_attribute("href")
            if site_url:
                print(f"✅ [{idx+1}] {site_url}")
                site_links.append(site_url)

        except Exception as e:
            print(f"❌ [{idx+1}] No site link found for this pin.")

    print(f"🎯 Done. Total site links collected: {len(site_links)}")

    return site_links
