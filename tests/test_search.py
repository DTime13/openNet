import pytest
from pages.home_page import HomePage
from behaviors.search_behavior import SearchBehavior

def test_guest_search(ctx):
	home = HomePage(ctx)

	home.go_to_homepage()

	search = home.nav.click_directory_button()
	search_behavior = SearchBehavior(search.ctx)
	search_behavior.search_and_go_to_specified_channel(username=None, current_page=search)

	driver.save_screenshot("screenshot/guest_search/live.png")

