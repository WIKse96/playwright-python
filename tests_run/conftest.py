import pytest
from playwright.sync_api import Playwright

@pytest.fixture
def page(playwright: Playwright): #playwright: Playwright zamien na page żeby uruchomi z konsoli i zakomentuj do page.goto
    browser = playwright.chromium.launch(headless=False) #zakomentuj
    context = browser.new_context()#zakomentuj
    page = context.new_page()#zakomentuj
    page.goto("https://demo.opencart.com")
    page.wait_for_load_state("networkidle")

    yield page
    browser.close()

