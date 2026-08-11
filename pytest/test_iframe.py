import time

from playwright.sync_api import Playwright, expect, sync_playwright

url = "https://practice-automation.com/iframes"


def test_iframe(playwright: Playwright) -> None:
    try:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()



    except Exception as e:
        print(f"Error: {e}")
    finally:
        context.close()
        browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        test_iframe(playwright)
