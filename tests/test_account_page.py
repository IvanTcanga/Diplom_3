from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure
from data import *
import time


class TestAccountPage:
	# @allure.title("Проверка переход по клику на «Личный кабинет»")
	# def test_go_to_recover_password_page(self, driver, create_and_delete_user):
	# 	email, password = create_and_delete_user
	# 	account_page = AccountPage(driver)
	# 	main_page = MainPage(driver)
	# 	main_page.click_button_log_in_account()
	# 	account_page.send_email_password(email, password)
	# 	account_page.click_login_button()
	# 	main_page.click_personal_account_link()
	# 	assert account_page.check_exit_button()

	# @allure.title("Проверка выход из аккаунта")
	# def test_go_to_recover_password_page(self, driver, create_and_delete_user):
	# 	email, password = create_and_delete_user
	# 	account_page = AccountPage(driver)
	# 	main_page = MainPage(driver)
	# 	main_page.click_button_log_in_account()
	# 	account_page.send_email_password(email, password)
	# 	account_page.click_login_button()
	# 	main_page.click_personal_account_link()
	# 	assert account_page.check_exit_button()

	@allure.title("Проверка переход в раздел «История заказов»")
	def test_go_to_history_orders(self, driver, create_and_delete_user):
		email, password = create_and_delete_user
		account_page = AccountPage(driver)
		main_page = MainPage(driver)
		main_page.click_button_log_in_account()
		account_page.send_email_password(email, password)
		account_page.click_login_button()
		main_page.click_personal_account_link()
		time.sleep(7)
		account_page.click_feed_button()
		assert account_page.check_history_feed()