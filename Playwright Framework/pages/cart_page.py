from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.remove_btn = page.locator("#remove-sauce-labs-backpack")
        self.checkout_btn = page.locator("#checkout")

    def remove_product(self):
        self.remove_btn.click()

    def checkout(self):
        self.checkout_btn.click()