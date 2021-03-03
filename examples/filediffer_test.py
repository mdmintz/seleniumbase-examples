"""
Testing https://www.developsense.com/exercises/fda/filediffer.html
"""

import os
from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_developsense_filediffer(self):
        self.demo_mode = True
        self.open("https://www.developsense.com/exercises/fda/filediffer.html")
        dir_name = os.path.dirname(os.path.abspath(__file__))
        file_path_1 = os.path.join(dir_name, "calendar_test.py")
        file_path_2 = os.path.join(dir_name, "kanban_test.py")
        self.get_element('input#fileInput1').send_keys(file_path_1)
        self.get_element('input#fileInput2').send_keys(file_path_1)
        self.click("input#diff")
        self.assert_text("No differences found", "div.diffinfo")
        self.click("input#clear2")
        self.get_element('input#fileInput2').send_keys(file_path_2)
        self.click("input#diff")
        self.assert_element('th:contains("Base Text")')
        self.assert_element('th:contains("New Text")')
        self.assert_element("#showDiff table tbody")
