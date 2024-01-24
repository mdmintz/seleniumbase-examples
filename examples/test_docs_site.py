from seleniumbase import BaseCase


class DocsSiteTests(BaseCase):
    def test_docs(self):
        self.demo_mode = True
        self.highlights = 2
        self.demo_sleep = 0.1
        self.message_duration = 0.25
        self.open("https://seleniumbase.io/examples/ReadMe/")
        self.assert_text("Running Example Tests", "h1")
        self.click('a[href$="/help_docs/customizing_test_runs/"]')
        self.assert_text("Command Line Options", "h1")
        self.click('a[href$="/examples/example_logs/ReadMe/"]')
        self.assert_text("Dashboard / Reports", "h1")
        self.click('a[href$="/help_docs/syntax_formats/"]')
        self.assert_text("Syntax Formats", "h1")
        self.click('a[href$="/recorder_mode/"]')
        self.assert_text("Recorder Mode", "h1")
        self.click('a[href$="/method_summary/"]')
        self.assert_text("API Reference", "h1")
        self.click('img[alt="logo"]')
        self.assert_text("SeleniumBase", "h1")
