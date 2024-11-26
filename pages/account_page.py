from pages.base_page import BasePage
import allure
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):
	@allure.step('Ввести Email и пароль')
	def send_email_password(self, email, password):
		self.send_keys_to_input(AccountPageLocators.EMAIL_INPUT_FIELD_LOGIN, email)
		self.send_keys_to_input(AccountPageLocators.PASSWORD_INPUT_FIELD_LOGIN, password)

	@allure.step('Кликнуть по кнопке "Войти"')
	def click_login_button(self):
		self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

	@allure.step('Кликнуть по кнопке "Лента заказов"')
	def click_feed_button(self):
		self.click_to_element(AccountPageLocators.FEED_BUTTON)

	@allure.step('Проверка отображения кнопки "Выход"')
	def check_exit_button(self):
		self.find_element_with_wait(AccountPageLocators.BUTTON_EXIT_FROM_ACCOUNT)
		return self.check_displaying_of_element(AccountPageLocators.BUTTON_EXIT_FROM_ACCOUNT)

	@allure.step('Проверка отображения выполненных заказов')
	def check_history_feed(self):
		self.find_element_with_wait(AccountPageLocators.HISTORY_FEED)
		return self.check_displaying_of_element(AccountPageLocators.HISTORY_FEED)
