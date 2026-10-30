from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        self.backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart = page.locator(".shopping_cart_link")

        self.menu = page.locator("#react-burger-menu-btn")
        self.logout_button = page.locator("#logout_sidebar_link")

    def add_backpack(self):
        self.backpack.click()

    def open_cart(self):
        self.cart.click()

    def logout(self):
        self.menu.click()
        self.page.wait_for_timeout(1000)
        self.logout_button.click()