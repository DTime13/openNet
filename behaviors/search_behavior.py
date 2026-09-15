from pages.search_page import SearchPage


class SearchBehavior:
	def __init__(self, ctx):
		self.ctx = ctx


	'''
	可以指定 USERNAME , 找不到會噴錯結束測試
	可以不指定 USERNAME , 預設進入第一間直播間
	'''
	def search_and_go_to_specified_channel(self, username = None, current_page=None):

		search_page = current_page if current_page else SearchPage(self.ctx)
		
		# 輸入搜尋字串
		search_page.search_by_text(username)

		# 搜尋後, 點擊 頻道 檢視全部
		search_page.click_expand_all_channels()

		# 向下捲動, 尋找特定直播間或頻道 by usename
		search_page.scroll_and_search_specified_user(username, 2)

		# 點擊特定直播間或頻道 by username
		search_page.go_to_specified_channel(username)


	def search_and_go_to_specified_category_page(self, category = None):
		pass


	def search_and_go_to_watch_specified_video(self, username = None):
		pass