#!/usr/bin/python3

import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

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
        h1_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEquals("inployment", h1_text.lower())

    def test_candidate_journey_is_correct(self):
        self.browser.get("localhost:8000")

        #Candidate logs in. Input box is hidden because reasons.
        input_id = "id_candidate_email"
        input_box = self.browser.find_element_by_id(input_id)
        input_label = self.browser.find_element_by_xpath(
            "//label[@for='" + input_id + "']"
        )

        # He notices, though, that there's a little arrow on each of the three
        # boxes
        arrow_class = '.arrow'
        arrows = self.browser.find_elements_by_css_selector(arrow_class)
        self.assertEqual(3, len(arrows),
                         msg="Not enough arrows visible on the screen")

        #He can't see a thanks box, cause he's not there yet.
        thanks_id = "thanks-box"
        with self.assertRaises(
                selenium.common.exceptions.NoSuchElementException
        ):
            self.browser.find_element_by_id(thanks_id)



        # He types his email in, and is shown a thanks box
        self.assertEquals("Email address:", input_label.text)
        input_box.send_keys("jubjub@crimson.fish")
        input_box.send_keys(Keys.ENTER)
        self.browser.find_element_by_id(thanks_id)

        # He clicks on the title, and the thanks box disappears
        self.browser.find_element_by_tag_name('h1').click()
        with self.assertRaises(
                selenium.common.exceptions.NoSuchElementException
        ):
            self.browser.find_element_by_id(thanks_id)



