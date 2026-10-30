from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect


def test_add_to_cart(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)

    inventory.add_backpack()

    inventory.open_cart()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

    page.wait_for_timeout(3000)