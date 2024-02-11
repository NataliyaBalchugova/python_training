# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.fill_contact(wd, Contact(firstname="Alexandr", lastname="Ponomarev", work="System Administrator",
                                      address="Demakova, 5"))
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, wd, username, password):
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def fill_contact(self, wd, contact):
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()

    def logout(self, wd):
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
    
    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
