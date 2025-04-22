from login_pinterest import login_and_save_cookies
from search_keywords import search_keywords
from scroll_pin_page import scroll_for_pins

def main():
    print("📌 Pinterest Automation Starting...")
    driver, wait = login_and_save_cookies(return_driver=True)

    if not driver or not wait:
        print("⚠️ Could not continue. Pinterest login or cookie load failed.")
        return

    print("🔍 Searching keywords...")
    search_keywords(driver, wait)

    print("📜 Scrolling and scraping pin URLs...")
    scroll_for_pins(driver, max_scrolls=20, output_file="pin_urls.txt")


    driver.quit()
    print("✅ Done. Pin URLs saved to pin_urls.txt")

if __name__ == "__main__":
    main()
