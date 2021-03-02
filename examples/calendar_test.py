"""
Testing https://developsense.com/calendar/calendar.html
Validate pop-up messages for actual vs expected values.
Expecting Success when [Earliest time] < [Latest time].
"""

from seleniumbase import BaseCase


class MyTestClass(BaseCase):

    def test_developsense_calendar(self):
        actual = [["*" for end in range(0, 48)] for start in range(0, 48)]
        expected = [["*" for end in range(0, 48)] for start in range(0, 48)]
        for start in range(1, 49):
            for end in range(1, 49):
                if start < end:
                    expected[start-1][end-1] = "1"  # Expected Success
                else:
                    expected[start-1][end-1] = "0"  # Expected Error

        self.open("https://developsense.com/calendar/calendar.html")
        self.type("#username", "SeleniumBase")

        print("\nPop-up status was incorrect for the following ranges:")
        timecode = {}
        for i in range(1, 49):
            timecode[i] = self.get_text('option[value="%s"]' % i)
        for start in range(1, 49):
            self.select_option_by_value("#starttime", str(start))
            for end in range(1, 49):
                self.select_option_by_value("#endtime", str(end))
                self.find_element("button#execute").click()
                text = self.switch_to_alert().text
                if "SUCCESS" in text:
                    actual[start-1][end-1] = "1"  # Actual Success
                else:
                    actual[start-1][end-1] = "0"  # Actual Error
                # Check if actual result matches expected result
                if actual[start-1][end-1] != expected[start-1][end-1]:
                    start_time = timecode[start]
                    end_time = timecode[end]
                    print("%s - %s" % (start_time, end_time))
