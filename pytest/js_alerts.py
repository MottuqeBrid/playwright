import time

from playwright.sync_api import Playwright, expect, sync_playwright

url = "https://the-internet.herokuapp.com/javascript_alerts"


def test_js_alerts(playwright: Playwright) -> None:
    try:
        browser = playwright.firefox.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.once("dialog", lambda dialog: dialog.accept())
        page.wait_for_timeout(3000)
        page.get_by_text("Click for JS Alert").click()
        page.wait_for_timeout(3000)
        expect(page.locator("#result")).to_have_text("You successfully clicked an alert")


    except Exception as e:
        print(f"Error: {e}")
    finally:
        context.close()
        browser.close()


def test_js_confirm(playwright: Playwright) -> None:
    try:
        browser = playwright.firefox.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.wait_for_timeout(3000)
        page.get_by_text("Click for JS Confirm").click()
        page.wait_for_timeout(3000)
        expect(page.locator("#result")).to_have_text("You clicked: Cancel")


    except Exception as e:
        print(f"Error: {e}")
    finally:
        context.close()
        browser.close()


def test_js_prompt(playwright: Playwright) -> None:
    try:
        browser = playwright.firefox.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)
        page.once("dialog", lambda dialog: dialog.accept("Hello World"))
        page.wait_for_timeout(3000)
        page.get_by_text("Click for JS Prompt").click()
        page.wait_for_timeout(3000)
        expect(page.locator("#result")).to_have_text("You entered: Hello World")


    except Exception as e:
        print(f"Error: {e}")
    finally:
        context.close()
        browser.close()


if __name__ == "__main__":
    with  sync_playwright() as playwright:
        test_js_alerts(playwright)
        test_js_confirm(playwright)
        test_js_prompt(playwright)
