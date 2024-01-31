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
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.NAME, "user").send_keys("admin")
        wd.find_element(By.NAME, "pass").send_keys("secret")
        wd.find_element(By.XPATH, "//input[@value='Login']").click()
        wd.find_element(By.LINK_TEXT, "groups").click()
        wd.find_element(By.XPATH, "//input[@value='New group']").click()
        wd.find_element(By.NAME, "group_name").send_keys("test")
        wd.find_element(By.NAME, "group_header").send_keys("1234")
        wd.find_element(By.NAME, "group_footer").send_keys("@#$%")
        wd.find_element(By.XPATH, "//input[@value='Enter information']").click()
        wd.find_element(By.LINK_TEXT, "Logout").click()
        # time.sleep(10)

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
