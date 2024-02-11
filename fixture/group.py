from selenium.webdriver.common.by import By

class GroupHelper:
    def __init__(self, app):
        self.app = app
    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
    def create(self, group):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//input[@value='New group']").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.XPATH, "//input[@value='Enter information']").click()


