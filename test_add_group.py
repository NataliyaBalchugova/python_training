# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.open_home_page()
        self.login(wd)
        self.open_groups_page(wd)
        self.create_group(wd)
        self.logout(wd)
        # time.sleep(10)

    def open_home_page(self):
        wd = self.open_home_page()
        self.open_home_page(wd)
        return wd
    def login(self, wd):
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
    def create_group(self, wd):
        # init group creation
        wd.find_element(By.XPATH, "//input[@value='New group']").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys("test")
        wd.find_element(By.NAME, "group_header").send_keys("1234")
        wd.find_element(By.NAME, "group_footer").send_keys("@#$%")
        wd.find_element(By.XPATH, "//input[@value='Enter information']").click()
    def open_groups_page(self, wd):
        wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self, wd):
        # Logout
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.is_alert_present()
            # self.wd.switch_to.alert()
        except NoAlertPresentException:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
