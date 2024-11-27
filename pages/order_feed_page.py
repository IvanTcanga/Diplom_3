from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
import allure


class OrderFeedPage(BasePage):
	@allure.step('Дождаться отображения заголовка Ленты заказов')
	def wait_and_check_displayed_title_of_orders_list(self):
		self.find_element_with_wait(OrderFeedPageLocators.TITLE_ORDER_FEED)
		return self.check_displaying_of_element(OrderFeedPageLocators.TITLE_ORDER_FEED)

	@allure.step('Кликнуть по первому заказу в ленте')
	def click_to_order_card(self):
		self.find_element_with_wait(OrderFeedPageLocators.FIRST_BURGER_CARD)
		self.click_to_element(OrderFeedPageLocators.FIRST_BURGER_CARD)

	@allure.step('Проверка отображение модального окна')
	def check_modal_window(self):
		self.find_element_with_wait(OrderFeedPageLocators.TITLE_MODAL_WINDOW)
		return self.check_displaying_of_element(OrderFeedPageLocators.TITLE_MODAL_WINDOW)





	@allure.step('Получить текст заголовка раздела заказов')
	def get_text_on_title_of_orders_list(self):
		return self.get_text_on_element(FeedPageLocators.title_of_orders_feed)

	@allure.step('Кликнуть по первому заказу в ленте')
	def click_on_order_card(self):
		self.wait_visibility_of_element(FeedPageLocators.order_in_feed)
		self.click_on_element(FeedPageLocators.order_in_feed)

	@allure.step('Получить текст заголовка окна с деталями заказа')
	def get_text_on_title_of_modal_order(self):
		return self.get_text_on_element(FeedPageLocators.title_of_modal_order)

	@allure.step('Получить количество заказов, выполненных за все время')
	def get_quantity_of_orders(self):
		self.find_element_with_wait(FeedPageLocators.quantity_of_orders)
		return self.get_text_on_element(FeedPageLocators.quantity_of_orders)

	@allure.step('Получить количество заказов, выполненных за сегодня')
	def get_daily_quantity_of_orders(self):
		self.find_element_with_wait(FeedPageLocators.daily_quantity_of_orders)
		return self.get_text_on_element(FeedPageLocators.daily_quantity_of_orders)

	@allure.step('Проверить наличие номера заказа в списке ленты')
	def check_id_order_in_feed(self, order_id):
		locator = FeedPageLocators.id_order_card_in_feed_with_substitutions
		locator_with_order_id = (locator[0], locator[1].format(order_id=order_id))
		self.find_element_with_wait(locator_with_order_id)
		return self.check_displaying_of_element(locator_with_order_id)

	@allure.step('Получить номер последнего заказа в разделе "В работе"')
	def get_order_number_in_feed_progress_section(self):
		return self.get_text_on_element(FeedPageLocators.number_of_order_in_progress)

