"""A SeleniumBase test that loads cookies to bypass login."""
from seleniumbase import SB

with SB(test=True, uc=True, user_data_dir="my_user_dir") as sb:
    sb.open("https://www.saucedemo.com")
    sb.wait_for_element("div.login_logo")
    sb.type("#user-name", "standard_user")
    sb.type("#password", "secret_sauce")
    sb.click('input[type="submit"]')
    sb.highlight("div.inventory_list", loops=6)
    sb.save_cookies(name="cookies.txt")

# Load previous saved cookies from udd to bypass login
with SB(test=True, uc=True, user_data_dir="my_user_dir") as sb:
    sb.open("https://www.saucedemo.com/inventory.html")
    sb.highlight("div.inventory_list", loops=12)
    sb.save_screenshot_to_logs()
