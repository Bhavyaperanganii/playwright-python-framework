from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect


def test_logout(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")

    page.wait_for_timeout(3000)