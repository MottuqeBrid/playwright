import re
from playwright.sync_api import Playwright, sync_playwright, expect

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
user_name = "Admin"
password = "admin123"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    page.get_by_placeholder("UserName").fill(user_name)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click(delay=1000)
    page.wait_for_timeout(2000)

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
