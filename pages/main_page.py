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

