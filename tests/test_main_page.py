import allure
from pages.main_page import MainPage


class TestMainPage:
    @allure.title("Проверка переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_recover_password_page(self, driver):
        recover_password_page = MainPage(driver)
        main_page = MainPage(driver)
        main_page.click_button_log_in_account()
        recover_password_page.click_button_recover_password()
        assert recover_password_page.check_displaying_of_p_question
