import re
from playwright.sync_api import Playwright, sync_playwright, expect

url = "https://www.goople.com"
password = "secret_sauce"
user_name = "standard_user"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
