# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
#from common import setUp

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class create_contact(unittest.TestCase):

    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_create_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd,username="admin",password="secret")
        self.open_contact_form(wd)
        self.fill_contact_form(wd,Contact(firstname="Inna",middlename="I",lastname="Makarenko",title="Ms",nickname="imakarenko",company="Vintelligent",address="Alton Pl",cellphone="",workphone="",email="",email2="",email3="",homepage="",anniversary="",birthday="1",birthmonth="January",birthyear="1980",homephone2="",address2="",homephone="123123123",notes="test contact"))
        self.submit_contact_form(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_id("header").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()
    def fill_contact_form(self, wd,contact):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        #if not wd.find_element_by_xpath(contact.birthday).is_selected():
        wd.find_element_by_name("bday").send_keys(contact.birthday)
        wd.find_element_by_name("bmonth").send_keys(contact.birthmonth)
        #if not wd.find_element_by_xpath(contact.birthmonth).is_selected():
        wd.find_element_by_name("byear").click()
        #wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthyear)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("test note")

    def submit_contact_form(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_form(self, wd):
        wd.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
