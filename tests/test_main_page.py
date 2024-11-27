import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestMainPage:
    # @allure.title("Проверка переход по клику на Конструктор»")
    # def test_go_to_constructor(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.click_button_log_in_account()
    #     main_page.click_constructor_button()
    #     assert main_page.check_title_make_burger

    # @allure.title("Проверка переход по клику на Лента заказов")
    # def test_go_to_feed_orders(self, driver):
    #     main_page = MainPage(driver)
    #     feed_page = OrderFeedPage(driver)
    #     main_page.click_feed_button()
    #     assert feed_page.wait_and_check_displayed_title_of_orders_list()

    # @allure.title("Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями")
    # def test_show_modal_win_details_after_click_on_ingredient(self, driver):
    #     main_page = MainPage(driver)
    #     feed_page = OrderFeedPage(driver)
    #     main_page.click_ingredient_from_constructor()
    #     assert main_page.check_details_ingredient_modal_window()

    # @allure.title('Всплывающее окно закрывается кликом по крестику')
    # def test_close_modal_window_details_of_ingredient_success(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.click_on_ingredient()
    #     main_page.close_modal()
    #     assert main_page.check_not_displaying_of_modal_details()
    #
    # @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    # def test_changing_counter_for_ingredients_in_order_success(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.drag_and_drop_ingredient_to_order()
    #     assert main_page.get_count_of_ingredients() == '2'
    #
    # @allure.title('залогиненный пользователь может оформить заказ')
    # def test_making_order_by_authenticated_user_success(self, driver, set_user_tokens):
    #     main_page = MainPage(driver)
    #     main_page.click_on_button_login_in_main()ls
    #     main_page.drag_and_drop_ingredient_to_order()
    #     main_page.click_on_button_make_order()
    #     assert main_page.check_displaying_of_confirmation_modal_of_order()