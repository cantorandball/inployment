#!/usr/bin/python3

import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_exists(self):
        self.browser.get("localhost:8000")

        # Check Inployment in the title
        self.assertIn("Inployment", self.browser.title)
