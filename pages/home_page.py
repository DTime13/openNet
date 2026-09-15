from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.navbar import NavbarComponent

class HomePage(BasePage):

	def __init__(self, ctx):
		super().__init__(ctx)

		self.url = self.ctx.config_data.get("Environment", "base_url")
		self.nav = NavbarComponent(self)


	def go_to_homepage(self):
		self.driver.get(self.url)

	def click_following_button(self):
		pass

	def click_live_button(self):
		pass