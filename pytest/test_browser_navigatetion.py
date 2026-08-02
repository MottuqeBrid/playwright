import re
from playwright.sync_api import Playwright, sync_playwright, expect

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
password = "secret_sauce"
user_name = "standard_user"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    page.locator("//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
