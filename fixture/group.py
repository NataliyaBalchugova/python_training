from selenium.webdriver.common.by import By
from model.group import Group
#from time import sleep


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.XPATH, "//input[@value='New group']").click()
        self.fill_group_form(group)
        wd.find_element(By.XPATH, "//input[@value='Enter information']").click()
        self.group_cache = None
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        # select first group
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def modify_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        # if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(By.NAME, "new")) > 0):
        if not (wd.current_url.endswith("/group.php")):
            self.open_groups_page()

        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            if not (wd.current_url.endswith("/group.php")):
                self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()


    def modify_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # open modification form
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(group)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None