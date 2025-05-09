# 🤖 Python With Selenium: Save & Load Cookies for Pinterest

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen?logo=selenium)](https://www.selenium.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Automate login, keyword search, scrolling, and internal pin URL scraping on Pinterest using Python & Selenium.

---

## 📂 Project Structure

| File                      | Purpose                                                        |
|---------------------------|----------------------------------------------------------------|
| `credentials.py`          | Stores Pinterest `EMAIL` and `PASSWORD`                        |
| `savecookies.py`          | Manual login → save cookies to `pinterest_cookies.pkl`         |
| `loadcookies.py`          | Auto login via cookies without manual sign-in                  |
| `login_pinterest.py`      | Handles login + optional cookie fallback                       |
| `main.py`                 | Master controller to run all automation                        |
| `search_keywords.py`      | Handles Pinterest keyword input and interaction                |
| `scroll_pin_page.py`      | Auto-scrolls page and scrapes `/pin/<pin_id>/` style URLs      |
| `scrape_site_links.py`    | (Optional) Extracts external site links from each pin (hover)  |
| `kw.txt`                  | List of keywords (1 per line)                                  |
| `pin_urls.txt`            | Output file with full Pinterest pin URLs                       |
| `old_pin_urls.txt`        | Backup of previous scraped URLs (if used)                      |
| `utils.py`                | Helper functions                                               |
| `pinterest_cookies.pkl`   | Binary cookie file (auto-generated by `savecookies.py`)        |

---

## ⚙️ How It Works

1. Run `savecookies.py` once to log in manually — cookies are saved.
2. Next runs skip login using cookies with `loadcookies.py`.
3. Bot reads keywords from `kw.txt`, searches them one-by-one.
4. Each keyword scrolls 20 times and scrapes internal `/pin/<id>/` URLs.
5. All results are saved to `pin_urls.txt`.

---

## 💻 Requirements

- Python 3.8+
- Selenium
- Firefox
- Geckodriver (must be in your system PATH)

### Install Dependencies

```bash
pip install selenium


## 🙌 Credits

Built with ❤️ by @thisisAhsanIqbal
SEO Consultant · Automation Developer · Instructor at FIRST (Akhuwat)
GitHub · LinkedIn(https://www.linkedin.com/in/ahsan-iqbal-digitalmarketingexpert/)
