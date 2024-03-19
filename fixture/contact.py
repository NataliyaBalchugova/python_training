from selenium.webdriver.common.by import By
from model.contact import Contact
from time import sleep
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
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
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
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        self.open_contact_page()
        self.select_contact_by_index(index)
        #print(f'before {len(self.contact_cache)}')
        self.delete_contact()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_first_contact(self, index, new_contact_data):
        wd = self.app.wd
        self.delete_contact_by_index(0)


    def delete_contact(self):
        wd = self.app.wd
        # delete contact
        #print('we are deleting first contact')
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None
        self.open_contact_page()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select contact
        # выбрали случайный контакт на основании случайного индекса
        selected_contact = wd.find_elements(By.NAME, "selected[]")[index]
        # кликнули по его чекбоксу
        selected_contact.click()
        # получаем айди выбраного контакта
        selected_id = selected_contact.get_attribute('id')
        # возвращаем числовое значение айди выбраного контакта
        return selected_id

    def modify_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contact_page()
        # edit contact
        # selected_id = self.select_contact_by_index(index)
        wd.get(f"http://localhost/addressbook/edit.php?id={self.select_contact_by_index(index)}")
        # wd.find_element(By.XPATH, '/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a')[index].click()
        # wd.find_elements(By.XPATH, '//img[@title="Edit"]')[index].click()
        # link = f"edit.php?={selected_id}"
        # wd.find_element(By.XPATH, f'//img[@href={link}]').click()
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
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("phone2", contact.secondaryphone)

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
#это мой варик из домашки
    # def get_contact_list(self):
    #     if self.contact_cache is None:
    #         wd = self.app.wd
    #         self.open_contact_page()
    #         self.contact_cache = []
    #         #for element in wd.find_elements(By.CSS_SELECTOR, "#maintable > tbody > tr:nth-child(2) > td:nth-child(3)"):
    #         for element in wd.find_elements(By.NAME, "selected[]"):
    #             text = element.text
    #             id = wd.find_element(By.NAME, "selected[]").get_attribute("id")
    #             self.contact_cache.append(Contact(firstname=text, id=id))
    #     return list(self.contact_cache)

# это варик Алексея Баранцева
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
                # id = cells[0].find_elements(By.NAME, "selected[]")
                id = wd.find_element(By.NAME, "selected[]").get_attribute("id")
                self.contact_cache.append(Contact(firstname=firstname,
                                                  lastname=lastname,
                                                  id=id,
                                                  all_phones_from_home_page=all_phones))
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
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.get(f"http://localhost/addressbook/edit.php?id={self.select_contact_by_index(index)}")

    # def numb_res(self):
    #     wd = self.app.wd
    #     return (wd.find_element(By.ID, 'search_count'))

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.get(f"http://localhost/addressbook/view.php?id={self.select_contact_by_index(index)}")
