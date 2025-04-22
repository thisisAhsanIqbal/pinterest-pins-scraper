import json

def load_cookies(driver, filename):
    with open(filename, "r") as file:
        cookies = json.load(file)

    for cookie in cookies:
        # Pinterest-specific fix:
        # Ensure cookie has required fields
        valid_cookie = {
            k: cookie[k] for k in cookie
            if k in ['name', 'value', 'path', 'domain', 'httpOnly', 'secure']
        }

        # Remove problematic fields
        for field in ['sameSite', 'expiry', 'same_site', 'priority']:
            cookie.pop(field, None)

        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"⚠️ Could not add cookie {cookie.get('name', '')}: {e}")
