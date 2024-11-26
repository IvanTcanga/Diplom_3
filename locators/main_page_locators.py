from selenium.webdriver.common.by import By


class MainPageLocators:

	SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, '//button[ text()="Войти в аккаунт" ]')  #кнопка входа в аккаунт

	CHECKOUT_BUTTON = (By.XPATH, '//button[ text()="Оформить заказ" ]')  #кнопка оформить заказ

	INVALID_PASSWORD_ERROR = (By.XPATH, '//p[ text()="Некорректный пароль" ]')  #ошибка неккоректный пароль

	PERSONAL_ACCOUNT_LINK = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')  #личный кабинет

	RESET_PASSWORD_LINK = (By.XPATH, '//a[ text()="Восстановить пароль" ]')  #ссылка на кнопку восстановить пароль


	CONSTRUCTOR_BUTTON = (By.XPATH, '//p[contains(text(),"Конструктор")]')  #constructor button

	ROLLS_h = (By.XPATH, '//span[text()="Булки"]/parent::div')  #раздел булки

	SAUCES_h = (By.XPATH, '//span[text()="Соусы"]/parent::div')  #раздел соусы

	FILLINGS_h = (By.XPATH, '//span[text()="Начинки"]/parent::div')  #раздел начинка

	LOGO_STELLAR_BURGER_MAIN_PAGE = (
	By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')  #logo stellar burger main page

	BUTTON_FEED_ORDERS = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

	INGREDIENT_LINK = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

