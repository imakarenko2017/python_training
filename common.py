from selenium.webdriver.firefox.webdriver import WebDriver

def setUp(self):
    self.wd = WebDriver(capabilities={"marionette": False})
    self.wd.implicitly_wait(60)

def open_home_page(self, wd):
    wd = self.wd
    wd.get("http://localhost/addressbook/")