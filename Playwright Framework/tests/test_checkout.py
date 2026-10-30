from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


def test_checkout(page):

    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_backpack()
    inventory.open_cart()

    cart = CartPage(page)
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.enter_details("Bhavya", "Test", "500001")
    checkout.finish_order()

    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

    page.wait_for_timeout(5000)