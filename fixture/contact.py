from selenium.webdriver.common.by import By
from model.contact import Contact
from time import sleep


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
        self.contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.open_contact_page()
        self.select_contact()
        print(f'before {len(self.contact_cache)}')
        self.delete_contact()


    def delete_contact(self):
        wd = self.app.wd
        # delete contact
        print('we are deleting first contact')
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None
        self.open_contact_page()

    def select_contact(self):
        wd = self.app.wd
        # select contact
        wd.find_element(By.NAME, "selected[]").click()


    def modify_firstname_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contact_page()
        # edit contact
        # edit_link = wd.find_element(By.NAME, 'selected[]').get_attribute('id')
        # wd.get(f"http://localhost/addressbook/edit.php?id={edit_link}")
        wd.find_element(By.XPATH, '//img[@title="Edit"]').click()
        # fill new data for firstname
        self.fill_contact_form(new_contact_data)
        # update contact
        # /html/body/div/div[4]/form[1]/input[1]
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        # return to contacts page
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None


    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("work", contact.work)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
        # if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
        # if not (wd.current_url.endswith("/group.php")):
        # self.open_contact_page()
        # return len(wd.find_elements(By.NAME, "selected[]"))
        return int(wd.find_element(By.XPATH, "/html/body/div/div[4]/label/strong/span").text)

    def el_exist(self):
        wd = self.app.wd
        self.open_contact_page()
        return (wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            #for element in wd.find_elements(By.CSS_SELECTOR, "#maintable > tbody > tr:nth-child(2) > td:nth-child(3)"):
            for element in wd.find_elements(By.NAME, "selected[]"):
                text = element.text
                id = wd.find_element(By.NAME, "selected[]").get_attribute("  ")
                self.contact_cache.append(Contact(firstname=text, id=id))
        return list(self.contact_cache)


    # def numb_res(self):
    #     wd = self.app.wd
    #     return (wd.find_element(By.ID, 'search_count'))

