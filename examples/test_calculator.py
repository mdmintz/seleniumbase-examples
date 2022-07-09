from seleniumbase import BaseCase


class CalculatorTests(BaseCase):
    def test_42_divided_by_7_equals_6(self):
        self.open("seleniumbase.io/apps/calculator")
        self.click("#clear")
        self.click('button[id="4"]')
        self.click('button[id="2"]')
        self.click("button#divide")
        self.click('button[id="7"]')
        self.click("button#equal")
        self.assert_exact_text("6", "input#output")

    def test_35_minus_21_equals_14(self):
        self.open("seleniumbase.io/apps/calculator")
        self.click("#clear")
        self.click('button[id="3"]')
        self.click('button[id="5"]')
        self.click("button#subtract")
        self.click('button[id="2"]')
        self.click('button[id="1"]')
        self.click("button#equal")
        self.assert_exact_text("14", "input#output")

    def test_6_times_7_plus_12_equals_54(self):
        self.open("seleniumbase.io/apps/calculator")
        self.click("#clear")
        self.click('button[id="6"]')
        self.click("button#multiply")
        self.click('button[id="7"]')
        self.click("button#add")
        self.click('button[id="1"]')
        self.click('button[id="2"]')
        self.click("button#equal")
        self.assert_exact_text("54", "input#output")

    def test_special_code(self):
        self.open("seleniumbase.io/apps/calculator")
        self.click("#clear")
        self.click('button[id="("]')
        self.click('button[id="0"]')
        self.click("button#add")
        self.click('button[id="0"]')
        self.click("button#add")
        self.click('button[id="0"]')
        self.click("button#add")
        self.click('button[id="0"]')
        self.click('button[id=")"]')
        self.click("button#equal")
        self.highlight('img[alt="SeleniumBase"]')
        self.click('a[href*="seleniumbase.io/apps/calculator"]')
        self.click("#clear")
        self.highlight('a[href*="seleniumbase.io/apps/calculator"]')
