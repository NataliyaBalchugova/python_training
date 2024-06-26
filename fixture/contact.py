from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
        wd.find_element(By.NAME, "work").send_keys(contact.workphone)
        wd.find_element(By.NAME, "home").send_keys(contact.homephone)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        wd.find_element(By.NAME, "phone2").send_keys(contact.secondaryphone)
        wd.find_element(By.NAME, "email").send_keys(contact.first_email)
        wd.find_element(By.NAME, "email2").send_keys(contact.second_email)
        wd.find_element(By.NAME, "email3").send_keys(contact.third_email)
        #sleep(3)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        #sleep(3)
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "work").send_keys(contact.workphone)
        wd.find_element(By.NAME, "home").send_keys(contact.homephone)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobilephone)
        wd.find_element(By.NAME, "phone2").send_keys(contact.secondaryphone)
        wd.find_element(By.NAME, "email").send_keys(contact.first_email)
        wd.find_element(By.NAME, "email2").send_keys(contact.second_email)
        wd.find_element(By.NAME, "email3").send_keys(contact.third_email)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        self.open_contact_page()
        self.select_contact_by_index(index)
        self.delete_contact()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact(self):
        wd = self.app.wd
        # delete contact
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None
        self.open_contact_page()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        selected_contact = wd.find_elements(By.NAME, "selected[]")[index]
        selected_contact.click()
        selected_id = selected_contact.get_attribute('id')
        return selected_id

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contact_page()
        # edit contact
        wd.get(f"http://localhost/addressbook/edit.php?id={self.select_contact_by_index(index)}")
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        # return to contacts page
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.first_email)
        self.change_field_value("email2", contact.second_email)
        self.change_field_value("email3", contact.third_email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count_contacts(self):
        wd = self.app.wd
        self.open_contact_page()
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
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                firstname = cells[1].text
                lastname = cells[2].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                # id = cells[0].find_elements(By.NAME, "selected[]")
                id = wd.find_element(By.NAME, "selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname,
                                                  lastname=lastname,
                                                  id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
                # print('break after 1st row')
                #break
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        first_email = wd.find_element(By.NAME, "email").get_attribute("value")
        second_email = wd.find_element(By.NAME, "email2").get_attribute("value")
        third_email = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       first_email=first_email, second_email=second_email, third_email=third_email
                       )

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.get(f"http://localhost/addressbook/edit.php?id={self.select_contact_by_index(index)}")

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        first_email = wd.find_element(By.XPATH, "/html/body/div/div[4]/a[1]").text
        second_email = wd.find_element(By.XPATH, "/html/body/div/div[4]/a[2]").text
        third_email = wd.find_element(By.XPATH, "/html/body/div/div[4]/a[3]").text
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone,
                       first_email=first_email, second_email=second_email, third_email=third_email)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.get(f"http://localhost/addressbook/view.php?id={self.select_contact_by_index(index)}")


    def delete_contact_by_id(self, id):
        self.open_contact_page()
        self.select_contact_by_id(id)
        self.delete_contact()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # select contact
        selected_contact = wd.find_element(By.NAME, "selected[]")
        selected_contact.click()
        selected_id = selected_contact.get_attribute('id')
        return selected_id

    def modify_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.get(f"http://localhost/addressbook/edit.php?id={self.select_contact_by_id(id)}")
        self.fill_contact_form(new_contact_data)
        # update contact
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        # return to contacts page
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def add_contact_in_group(self, id):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//input[@value='Add to']").click()
