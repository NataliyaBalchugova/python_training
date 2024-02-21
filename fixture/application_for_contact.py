from selenium import webdriver
from selenium.webdriver.common.by import By


class ApplicationContact:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")

    def login(self, username, password):
        wd = self.wd
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def fill_contact(self, contact):
        wd = self.wd
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact.work)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()
        wd.find_element(By.LINK_TEXT, "home").click()

    def logout(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element(By.LINK_TEXT, "Logout").click()

    #def is_element_present(self, how, what):
       #  try:
            #self.wd.find_element(by=how, value=what)
       # except NoSuchElementException:
           # return False
       # return True

    # def is_alert_present(self):
        #try:
           # self.wd.switch_to_alert()
        #except NoAlertPresentException:
          #  return False
        #return True

    def destroy(self):
        self.wd.quit()
