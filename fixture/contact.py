
class ContactHelper:

    def __init__(self,  app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_form()
        self.fill_contact_form(contact)
        self.submit_contact_form()

    def is_exist(self,firstname,lastname):
        wd = self.app.wd
        try:
            wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox'][@title='Select (" + firstname + " " + lastname + ")']").click()
            return True
        except:
            return False

    def count(self):
        wd=self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def open_contact_form(self):
        wd=self.app.wd
        wd.find_element_by_name("add new").click()

    def change_field_value(self, field_name, text):
        wd=self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            if str(field_name) is not "bday" and str(field_name) is not "bmonth":
                wd.find_element_by_name(field_name).clear()
                wd.find_element_by_name(field_name).send_keys(text)
            else:
                wd.find_element_by_xpath("//select[@name='" + field_name + "']/option[@value='" +text + "']").click()

    def modify_first_contact(self, new_contact_data):
        wd=self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//img[@title='Edit']").click()
        self.fill_contact_form(new_contact_data)
        self.submit_contact_form()

    def open_contacts_page(self):
        wd=self.app.wd
        if wd.current_url.endswith("edit.php"):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd=self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox']").click()
        #wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox'][@title='Select (" + firstname + " " + lastname + ")']").click()
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to_alert().accept()




    def fill_contact_form(self, contact):
        wd=self.app.wd
        # fill contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("email", contact.email)
        self.change_field_value("bday", contact.birthday)
        self.change_field_value("bmonth", contact.birthmonth)
        self.change_field_value("byear", contact.birthyear)
        self.change_field_value("bday", contact.birthday)
        self.change_field_value("notes", contact.notes)


    def submit_contact_form(self):
        wd = self.app.wd
        if wd.current_url.find("/edit.php?id=")>=0:
            wd.find_element_by_xpath("//input[@name='update'][@value='Update']").click()
        else:
            wd.find_element_by_xpath("//input[@name='submit'][@value='Enter']").click()

    def open_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

