import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.google.com/?zx=1785599076480")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("playwright")

    # ---------------------
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
