# scroll_pin_page.py

import time
from selenium.webdriver.common.by import By

def scroll_for_pins(driver, max_scrolls=20, output_file="pin_urls.txt"):
    print("📜 Scrolling and scraping Pinterest pin URLs...")

    seen_urls = set()

    with open(output_file, "w", encoding="utf-8") as f:
        for scroll_num in range(1, max_scrolls + 1):
            print(f"🔁 Scroll {scroll_num} → Scrolling page...")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2.5)

            # Fetch only visible anchor links after this scroll
            pin_links = driver.find_elements(By.XPATH, "//a[contains(@href, '/pin/') and @href]")

            new_urls = []
            for link in pin_links:
                try:
                    href = link.get_attribute("href")
                    if href and "/pin/" in href:
                        full_url = href if href.startswith("http") else "https://www.pinterest.com" + href
                        if full_url not in seen_urls:
                            seen_urls.add(full_url)
                            new_urls.append(full_url)
                except Exception:
                    continue  # if stale, just skip

            print(f"🧲 Scroll {scroll_num}: {len(new_urls)} new pin URLs found")

            if new_urls:
                f.write(f"\n# Scroll {scroll_num} – {len(new_urls)} new pins\n")
                for url in new_urls:
                    f.write(url + "\n")
                f.flush()

    print(f"✅ Scraping complete! Total unique pins collected: {len(seen_urls)}")
