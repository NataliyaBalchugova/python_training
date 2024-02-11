from selenium import webdriver
from selenium.webdriver.common.by import By

class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, user_name, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(user_name)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def create_group(self, group):
        wd = self.wd
        wd.find_element(By.XPATH, "//input[@value='New group']").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.XPATH, "//input[@value='Enter information']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()

