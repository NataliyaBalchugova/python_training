from selenium.webdriver.common.by import By
#from model.contact import Contact
#from fixture.session import SessionHelper
# from fixture.application import Application


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def fill_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()


    def delete_first_contact(self):
        #wd = self.app.wd
        self.open_contact_page()
        self.select_contact()
        self.delete_contact()

    def delete_contact(self):
        wd = self.app.wd
        # delete contact
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()

    def select_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element(By.NAME, "selected[]").click()
