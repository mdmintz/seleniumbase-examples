from seleniumbase import BaseCase
BaseCase.main(__name__, __file__, "--rs", "--xvfb")


class MyTestClass(BaseCase):
    def test_swag_labs_1(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.assert_element("div.inventory_list")

    def test_swag_labs_2(self):
        self.click('button[name*="backpack"]', timeout=1)
        self.click("#shopping_cart_container a")
        self.assert_text("Backpack", "div.cart_item")

    def test_swag_labs_3(self):
        self.click("button#checkout", timeout=1)
        self.type("input#first-name", "SeleniumBase")
        self.type("input#last-name", "Automation")
        self.type("input#postal-code", "77123")
        self.click("input#continue")
        self.click("button#finish")
        self.assert_text("Thank you for your order!")
