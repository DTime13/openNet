
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AppContext:
	def __init(self, driver, config_data=None):
		self.driver = driver
		self.config_data = config_data

class BasePage:
	def __init__(self, driver, ctx: AppContext):
		self.ctx = ctx
		self.driver = ctx.driver
		self.timeout = ctx.config_data.getint("Environment", "timeout") if ctx.config_data else 5


	def find_element(self, locator):
		return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

	def find_elements(self, locator):
		return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

	def click(self, locator):
		self.find_element(locator).click()

	def send_keys(self, locator, text, is_clear=True, press_enter=True):
		elem = self.find_element(locator)

		if is_clear:
			elem.clear()

		elem.send_keys(text)

		if press_enter:
			elem.send_keys(Keys.ENTER)


	def scroll_to_bottom(self):
		self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


	def wait_until_invisible(self, locator):
		return WebdriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))


	def hover_to_element(self, locator):
		element = self.find_element(locator)
		actions = ActionChains(self.driver)
		actions.move_to_element(element).perform()

	def switch_to_iframe(self, iframe_locator):
		WebDriverWait(self.driver, self.timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))


	def switch_to_window(self):
		self.driver.switch_to.default_content()
