from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
	@allure.step('Кликнуть по кнопке "Войти в аккаунт" на главной')
	def click_button_log_in_account(self):
		self.click_to_element(MainPageLocators.SIGN_IN_ACCOUNT_BUTTON)

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

	@allure.step('Кликнуть по ингредиенту в конструкторе')
	def check_details_ingredient_modal_window(self):
		self.find_element_with_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
		return self.check_displaying_of_element(MainPageLocators.DETAILS_OF_INGREDIENT)
