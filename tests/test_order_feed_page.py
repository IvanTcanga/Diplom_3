from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
import allure


class TestOrderFeedPage:
	@allure.step('Eсли кликнуть на заказ, откроется всплывающее окно с деталями')
	def test_opening_modal_window(self, driver):
		feed_page = OrderFeedPage(driver)
		main_page = MainPage(driver)
		main_page.click_feed_button()
		# feed_page.wait_title_of_orders_list()
		feed_page.click_to_order_card()
		assert feed_page.check_modal_window()

