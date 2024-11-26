from pages.recover_password_page import RecoverPasswordPage
from pages.main_page import MainPage
import allure


class TestRecoverPasswordPage:
	@allure.title("Проверка переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
	def test_go_to_recover_password_page(self, driver):
		recover_password_page = RecoverPasswordPage(driver)
		main_page = MainPage(driver)
		main_page.click_button_log_in_account()
		recover_password_page.click_button_recover_password()
		assert recover_password_page.check_displaying_of_p_question

	@allure.title("Проверка перехода на url reset_password,после ввод почты и клика по кнопке «Восстановить")
	def test_go_to_reset_password_page(self, driver):
		recover_password_page = RecoverPasswordPage(driver)
		main_page = MainPage(driver)
		main_page.click_button_log_in_account()
		recover_password_page.click_button_recover_password()
		recover_password_page.send_data_email()
		recover_password_page.click_button_recover()
		assert recover_password_page.check_displaying_of_save_button

	@allure.title("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
	@allure.description("При клике по иконке показать/скрыть значение атрибута инпута становится 'password'")
	def test_active_border_after_click_icon(self, driver):
		recover_password_page = RecoverPasswordPage(driver)
		main_page = MainPage(driver)
		main_page.click_button_log_in_account()
		recover_password_page.click_button_recover_password()
		recover_password_page.send_data_email()
		recover_password_page.click_button_recover()
		recover_password_page.wait_visibility_of_icon()
		recover_password_page.click_icon()
		assert recover_password_page.check_displaying_active_border()
