from selenium.webdriver.common.by import By

class NavbarComponent:

	LOBBY_BUTTON = (By.CSS_SELECTOR, "div#root .tw-transition a")

	DIRECTORY_BUTTON = (By.CSS_SELECTOR, "div#root .tw-transition a[href$='directory']")

	ACTIVITY_BUTTON = (By.CSS_SELECTOR, "div#root .tw-transition a[href$='activity']")

	HOME_BUTTON = (By.CSS_SELECTOR, "div#root .tw-transition a[href$='home']")

	
	def __init__(self, page_instance):
		self.page = page_instance


# 點擊 創作者大廳

	def click_lobby_button(self):
		pass


# 點擊 搜尋

	def click_directory_button(self):
		self.page.click(DIRECTORY_BUTTON)
		from pages.search_page import SearchPage
		return SearchPage(self.page.ctx)


# 點擊 活動紀錄

	def click_search_button(self):
		pass


# 點擊 個人檔案

	def click_search_button(self):
		pass
