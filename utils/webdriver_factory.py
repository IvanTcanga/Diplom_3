from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


class WebdriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == 'chrome':
            firefox_options = FirefoxOptions()
            profile = FirefoxProfile()
            profile.set_preference("browser.privatebrowsing.autostart", True)
            firefox_options.profile = profile
            return webdriver.Firefox(options=firefox_options, service=FirefoxService())
        elif browser == 'firefox':
            chrome_options = Options()
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--incognito')
            return webdriver.Chrome(options=chrome_options, service=ChromeService())
