from pages.login_page import LoginPage
from playwright.sync_api import expect


def test_login(page):

    login = LoginPage(page)

    login.open()

    page.wait_for_timeout(2000)

    login.login("standard_user", "secret_sauce")

    page.wait_for_timeout(3000)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    page.wait_for_timeout(3000)