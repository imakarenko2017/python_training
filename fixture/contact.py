

class ContactHelper:

    def __init__(self,  app):
        self.app = app


    def open_contact_form(self):
        wd=self.app.wd
        wd.find_element_by_name("add new").click()

    def modify(self, contact):
        wd=self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_xpath("//input[@name='update'][@type='submit']").click()

    def delete(self, contact):
        wd=self.app.wd
        wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox']").click()
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to_alert().accept()




    def fill_contact_form(self, contact):
        wd=self.app.wd
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

    def submit_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

