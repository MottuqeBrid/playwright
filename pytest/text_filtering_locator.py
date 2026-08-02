import re
from playwright.sync_api import Playwright, sync_playwright, expect

url = "https://www.saucedemo.com/"
password = "secret_sauce"
user_name = "standard_user"


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    page.locator("#user-name").fill(user_name, timeout=2000)
    page.locator("#password").fill(password, timeout=2000)
    page.locator("#login-button").click()

    product_header = page.locator("//span[text()='Products']")
    assert product_header.is_visible(), "User is unable to login"

    # product1 = page.locator(".inventory_item").filter(has_text="Sauce Labs Bike Light")
    product1 = page.locator(".inventory_item").filter(has=page.locator("button.btn_inventory "))
    product1.first.locator("button").click()
    page.wait_for_timeout(5000)

    # burger_menu = page.locator("#react-burger-menu-btn")
    # page.pause()
    # burger_menu.click()
    # logout_btn = page.locator("#logout_sidebar_link")
    # assert logout_btn.is_visible(), "Logout button is not visible"
    # page.pause()
    # logout_btn.click()
    #
    # login_btn = page.locator("#login-button")
    # assert login_btn.is_visible(), "Login button is not visible"

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
