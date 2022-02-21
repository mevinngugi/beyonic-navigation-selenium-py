"""
This module contains page setup to crawl through
beyonic website starting from the homepage
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BeyonicHomePage:

    # URL
    URL = "https://www.beyonic.com/"

    # Initialize the class
    def __init__(self, browser):
        self.browser = browser

    # Page Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def get_current_url(self):
        current_url = self.browser.current_url
        return current_url

    # Navigates through the pages captured by the link_text list
    # and returns the current url
    def navigation(self, link_text):
        parent_handle = self.browser.current_window_handle
        self.browser.find_element(By.LINK_TEXT, link_text).click()
        all_handles = self.browser.window_handles
        for handle in all_handles:
            if handle != parent_handle:
                self.browser.switch_to.window(handle)
                self.get_current_url()

    def click_login(self):
        self.browser.find_element(By.CLASS_NAME, "primary-btn").click()
