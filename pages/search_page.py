from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.navbar import NavbarComponent

class SearchPage(BasePage):

	SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='search']")
	EXPAND_ALL_CHANNELS = (By.CSS_SELECTOR, "section>div a[href$='type=channels']")
	EXPAND_ALL_CATEGORIES = (By.CSS_SELECTOR, "section>div a[href$='type=categories']")
	EXPAND_ALL_VIDEOS = (By.CSS_SELECTOR, "section>div a[href$='type=videos']")

	SPECIFIED_LIVE = "div[role='list']>div button h2[title={username}]"
	SPECIFIED_CHANNEL = "div[role='list']>div a[href$={username}]"

	def __init__(self, ctx):
		super().__init__(ctx)
		self.nav = NavbarComponent(self)


# 搜尋前, 點擊 分類 按鈕

	# 搜尋前, 取得 分類 列表

	# 搜尋前, 點擊 特定分類 前往該分類頁面


# 搜尋前, 點擊 live 頻道 按鈕

	# 搜尋前, 取得 live 頻道 清單

	# 搜尋前, 點擊 特定 live 頻道 前往該分類頁面


# 輸入搜尋字串  ****
	def search_by_text(self, text, is_clear=True):
		send_keys(self.SEARCH_FIELD, text, is_clear)
		elems = find_elements(By.CSS_SELECTOR, "section")
		assert elems != True, f"Search Page: No search result about '{text}'"


	# 取得頻道清單

	# 點擊 特定頻道 進入直播間 by username (default 第一間)

	# 取得分類清單

	# 點擊分類清單 進入該分類頁面 by category (default 第一個)

	# 取得影片清單

	# 點擊特定影片 進入撥放該影片 by username (default 第一間)
	

	# 搜尋後, 點擊 頂端 按鈕


		# 搜尋後, 點擊 頻道 檢視全部(結果同 點擊 頻道 按鈕) ***
	def click_expand_all_channels(self):
		click(self.EXPAND_ALL_CHANNELS)


			# 向下捲動, 尋找特定直播間或頻道 by usename (default 捲動 2 次) ***
	def scroll_and_search_specified_user(self, username=False, searchTimes = 2)

		specified_live = self.SPECIFIED_LIVE.format(username=username)
		specified_channel = self.SPECIFIED_CHANNEL.format(username=username)


		for times in range(searchTimes):
			if username:
				live_elems = find_elements(By.CSS_SELECTOR, specified_live)
				channels_elems = find_elements(By.CSS_SELECTOR, specified_channel)
				if live_elems || channels_elems:
					break
				else:
					assert times == searchTimes, f"SearchPage: Can't find the search result about {username}"

			scroll_to_bottom()
			time.sleep(2)


			# 點擊特定直播間或頻道 by username (default 第一間直播間)  ***
	def go_to_specified_channel(self, username=False)

		specified_live = self.SPECIFIED_LIVE.format(username=username)
		specified_channel = self.SPECIFIED_CHANNEL.format(username=username)
		
		if username:

			'''判斷是否找到指定 user 資料 >> 找到點擊並前往 >> 找不到噴錯 '''

			live_elems = find_elements(By.CSS_SELECTOR, specified_live)
			channels_elems = find_elements(By.CSS_SELECTOR, specified_channel)
			
			if live_elems:
				click(By.CSS_SELECTOR, specified_live)
				from pages.live_page import LivePage
				return LivePage(self.driver)
			
			else if channels_elems:
				click(By.CSS_SELECTOR, specified_channel)
				from pages.channel_page import ChannePage
				return ChannelPage(self.driver)
			
			else
				pytest.fail(f"SearchPage: Can't find the search result about {username}")

		''' 未指定 user 時, 前往列表上第一間直播間 '''

		click(By.CSS_SELECTOR, f"div[role='list']>div button")
		from pages.live_page import LivePage
		return LivePage(self.driver)



		# 搜尋後, 點擊 影片 檢視全部(結果同 點擊 頻道 按鈕)


		# 搜尋後, 點擊 分類 檢視全部(結果同 點擊 頻道 按鈕)


	# 搜尋後, 點擊 頻道 按鈕


	# 搜尋後, 點擊 分類 按鈕


	# 搜尋後, 點擊 影片 按鈕



# 取得搜尋紀錄

# 點擊特定搜尋紀錄(重新搜尋)

# 刪除特定搜尋紀錄

# 刪除所有搜尋紀錄

# 頁面回捲至 top


'''
function list backup

# 搜尋前, 點擊 分類 按鈕

	# 搜尋前, 取得 分類 列表

	# 搜尋前, 點擊 特定分類 前往該分類頁面

# 搜尋前, 點擊 live 頻道 按鈕

	# 搜尋前, 取得 live 頻道 清單

	# 搜尋前, 點擊 特定 live 頻道 前往該分類頁面

# 輸入搜尋字串  ****

	# 取得頻道清單

	# 點擊 特定頻道 進入直播間 by username (default 第一間)

	# 取得分類清單

	# 點擊分類清單 進入該分類頁面 by category (default 第一個)

	# 取得影片清單

	# 點擊特定影片 進入撥放該影片 by username (default 第一間)

	# 搜尋後, 點擊 頂端 按鈕

		# 搜尋後, 點擊 頻道 檢視全部(結果同 點擊 頻道 按鈕) ***

			# 向下捲動, 尋找特定直播間 by usename (default 捲動至搜索數量 > 20) ***

			# 點擊特定直播間 by username (default 第一間)  ***

		# 搜尋後, 點擊 影片 檢視全部(結果同 點擊 頻道 按鈕)

		# 搜尋後, 點擊 分類 檢視全部(結果同 點擊 頻道 按鈕)

	# 搜尋後, 點擊 頻道 按鈕

	# 搜尋後, 點擊 分類 按鈕

	# 搜尋後, 點擊 影片 按鈕

# 取得搜尋紀錄

# 點擊特定搜尋紀錄(重新搜尋)

# 刪除特定搜尋紀錄

# 刪除所有搜尋紀錄

# 頁面回捲至 top

'''
