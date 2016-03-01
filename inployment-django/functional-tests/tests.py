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

        # Check Inployment in the title and h1
        self.assertIn("Inployment", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEquals("inployment", header_text.lower())

    def test_candidate_journey_is_correct(self):
        self.browser.get("localhost:8000")

        #Candidate logs in. Input box is hidden because reasons
        input_id = "id_candidate_email"
        input_box = self.browser.find_element_by_id(input_id)
        input_label = self.browser.find_element_by_xpath(
            "//label[@for='" + input_id + "']"
        )

        self.assertEquals("Email address:", input_label.text)


