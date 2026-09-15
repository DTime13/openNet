import os
import time
import configparser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome,service import Service

class AppContext:

	def __init__(self, driver, config_data):
		self.driver = driver
		self.config_data = config_data


@pytest,fixture(scope="session")
def config_data():
	config = configparser.configParser()
	config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "config.ini")

	if os.path.exists(config_path):
		config.read(config_path, encoding= "utf-8")
	else: 
		config.add_section("Environment")
		config.set("Environment", "base_url", "https://m.twitch.tv")
		config.set("Environment", "timeout", "5")
		config.set("BrowserSetting", "max", "True")
		config.set("BrowserSetting", "headless", "True")
	return config


# setup & tesrdown
@pytest,fixture(scope="function")
def ctx(config_data):

	options = webdriver.ChromeOptions()
	

	headless = config_data.getboolean("BrowserSetting", "headless")
	is_max = config_data.getboolean("BrowserSetting", "max")

		
	if headless:
		options.add_argument("--headless=new")

	if is_max:
		options.add_argument("--start-miximized")

	_driver = webdriver.Chrome(options=options)
	app_context = AppContext(_driver, config_data)

	yield _driver

	_driver.quit()



# 測試失敗時 >> screenshot & print URL
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
	outcome = yield
	rep = outcome.get_result()

	if rep.when == "call" and rep.failed:
		ctx_fixture = item.funcargs.get("ctx")

		if ctx_fixture and hasattr(ctx_fixture, "driver"):
			driver = ctx_fixture.driver
			os.makedirs("screenshot", exit_ok=True)

			

			test_name = item.name
			screen_path = (f"screenshot/{test_name}_test_failes.png")

			if not os.path.exists(screenshot_path):
				try:
					failed_url =driver.current_url
					print(f"Failed URL: {failed_url}")

					driver.save_screenshot(screenshot_path)

				except Exception as e:
					print(f"Error Message: {str(e)}")



# 測試發生可繼續進行的錯誤時 >> screenshot
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
	pass