"""
This module contains tests covering the navigation of the beyonic website.
"""

import pytest
from pages.beyonic_homepage import BeyonicHomePage


def test_loaded_homepage(browser):
    homepage = BeyonicHomePage(browser)
    HOMEPAGE_URL = "https://www.beyonic.com/"
    homepage.load()
    assert HOMEPAGE_URL == homepage.get_current_url()


# Navigates to every page defined by link text in the list.
@pytest.mark.parametrize(
    "link_text", ["Features", "About", "Use case", "Pricing", "Testimonials"]
)
def test_page_navigation(browser, link_text):
    homepage = BeyonicHomePage(browser)
    homepage.load()
    homepage.navigation(link_text)
    # assert homepage.config["homepage_url"] == homepage.get_current_url()
    assert link_text.lower() in homepage.get_current_url()
