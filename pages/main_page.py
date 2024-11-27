from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
	@allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
	def click_button_log_in_account(self):
		self.click_to_element(MainPageLocators.SIGN_IN_ACCOUNT_BUTTON)

	@allure.step('Кликнуть по кнопке "Оформить заказ" на главной')
	def click_checkout_button(self):
		self.click_to_element(MainPageLocators.CHECKOUT_BUTTON)

	@allure.step('Кликнуть по кнопке "Личный кабинет" на главной')
	def click_personal_account_link(self):
		self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT_LINK)

	@allure.step('Проверка видимости кнопки Оформить заказ')
	def wait_visible_checkout_button(self):
		self.find_element_with_wait(MainPageLocators.CHECKOUT_BUTTON)

	@allure.step('Кликнуть по кнопке "Лента заказов"')
	def click_feed_button(self):
		self.find_element_with_wait(MainPageLocators.FEED_BUTTON)
		self.click_to_element(MainPageLocators.FEED_BUTTON)

	@allure.step('Кликнуть по кнопке конструктора')
	def click_constructor_button(self):
		self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

	@allure.step('Проверка отображение заголовка "Соберите бургер"')
	def check_title_make_burger(self):
		return self.click_to_element(MainPageLocators.MAKE_BURGER_TITLE)

	@allure.step('Кликнуть по ингредиенту в конструкторе')
	def click_ingredient_from_constructor(self):
		self.find_element_with_wait(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)
		self.click_to_element(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)

	@allure.step('Проверка,что модальное окно "Детали ингредиента" появилось')
	def check_details_ingredient_modal_window(self):
		self.find_element_with_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
		return self.check_displaying_of_element(MainPageLocators.DETAILS_OF_INGREDIENT)

	@allure.step('Клик по крестику для закрытия модального окна "Детали ингредиента"')
	def close_modal_window_details_ingredient(self):
		self.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW_DETAILS_ING)
		self.click_to_element(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW_DETAILS_ING)

	@allure.step('Проверка,что модальное окно "Детали ингредиента" закрыто')
	def check_details_ingredient_modal_window_closed(self):
		self.find_element_with_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
		return not self.check_displaying_of_element(MainPageLocators.DETAILS_OF_INGREDIENT)

	@allure.step('Перетащить ингредиент в конструктор бургера в корзине')
	def drag_and_drop_ingredient_to_basket(self):
		from_element = self.find_element_with_wait(MainPageLocators.INGREDIENT_FROM_CONSTRUCTOR)
		to_element = self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_BASKET)
		self.drag_and_drop_element(from_element, to_element)

	@allure.step('Получием каунтер добавленных ингредиентов')
	def get_counter_of_ingredients_in_basket(self):
		return self.get_text_from_element(MainPageLocators.COUNTER_INGREDIENT_IN_BASKET)

	@allure.step('Проверить отображение окна о создании заказа')
	def check_displaying_of_modal_window_after_create_order(self):
		self.find_element_with_wait(MainPageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)
		return self.check_displaying_of_element(MainPageLocators.MODAL_WINDOW_AFTER_CREATE_ORDER)

	@allure.step("Закрытие окна заказа")
	def close_order_window(self):
		close_button = self.find_element_with_wait(MainPageLocators.CLOSE_MOD_WINDOW_AFTER_CREATE_ORDER)
		self.click_on_element_js(close_button)

	@allure.step('Получить номер заказа в модальном окне после создания заказа')
	def get_number_in_modal_window_after_create_order(self):
		self.wait_for_element_to_change_text(MainPageLocators.NINES_IN_MOD_WIN_AFTER_CREATE_ORDER, '9999')
		return self.get_text_from_element(MainPageLocators.NINES_IN_MOD_WIN_AFTER_CREATE_ORDER)

