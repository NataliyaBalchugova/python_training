from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:


    def __init__(self, browser="firefox"):
        if browser == "firefox":
            # service = FirefoxService(executable_path='./geckodriver.exe')
            self.wd = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser == "chrome":
            self.wd = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False




    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()

