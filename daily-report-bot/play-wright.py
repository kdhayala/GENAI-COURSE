from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.accuweather.com/en/in/chennai/206671/hour")
    page.screenshot(path="screenshot.png")
    browser.close()