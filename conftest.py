import pytest
from utils.webdriver_factory import WebdriverFactory
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import allure
from utils.helper import *
from selenium import webdriver


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.get(URLs.BASE_URL)
    yield driver
    driver.quit()



# @allure.title('Используем фабрику WebdriverFactory для инициализации браузера в зависимости от названия')
# @pytest.fixture(params=['chrome', 'firefox'], ids=['chrome', 'firefox'])
# def driver(request):
#     browser = request.param
#     driver = WebdriverFactory.get_driver(browser)
#     driver.get(URLs.BASE_URL)
#     yield driver
#     driver.quit()
#
#
@pytest.fixture
@allure.title('Создание и удаление тестового пользователя')
def create_and_delete_user():
    payload, response = auth_user_and_get_creds()
    email = payload.get('email')
    password = payload.get('password')
    yield email, password
    access_token = response.json().get('accessToken')
    requests.delete(f'{URLs.BASE_URL}{URLs.DELETE_USER_URL}', headers={'Authorization': access_token})



# @pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
# def driver(request):
#     driver_class = request.param
#     if driver_class == webdriver.Chrome:
#         options = Options()
#         options.add_argument('--window-size=1920,1080')
#         options.add_argument('--incognito')
#         driver = webdriver.Chrome(options=options)
#     elif driver_class == webdriver.Firefox:
#         firefox_options = webdriver.FirefoxOptions()
#         firefox_options.add_argument('--width=1920')
#         firefox_options.add_argument('--height=1080')
#         profile = FirefoxProfile()
#         profile.set_preference("browser.privatebrowsing.autostart", True)
#         firefox_options.profile = profile
#         driver = webdriver.Firefox(options=firefox_options)
#     driver.get(Urls.base_url)
#     yield driver
#     driver.quit()