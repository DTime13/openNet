from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.navbar import NavbarComponent

class LivePage(BasePage):

	BODY_LOADING = (By.CSS_SELECTOR, "body[class^=ReactModal]")


	def __init__(self, ctx):
		super().__init__(ctx)
		self.nav = NavbarComponent(self)

		WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(self.BODY_LOADING))
		self.wait_until_invisible(self.BODY_LOADING)

	def left_comment(self, text):
		pass