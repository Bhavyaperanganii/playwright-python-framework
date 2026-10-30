from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect


def test_remove_cart(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(page)
    cart.remove_product()

    expect(page.locator(".cart_item")).to_have_count(0)

    page.wait_for_timeout(3000)