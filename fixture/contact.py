from selenium.common.exceptions import NoSuchElementException
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self,  app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_form()
        self.fill_contact_form(contact)
        self.submit_contact_form()
        self.contact_cache = None


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
        if not wd.current_url.endswith('/edit.php'):
            wd.find_element_by_xpath("//a[text()='add new']").click()

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
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd=self.app.wd
        self.open_contacts_page()
        element = wd.find_elements_by_xpath("//img[@title='Edit']")
        element[index].click()
        self.fill_contact_form(new_contact_data)
        self.submit_contact_form()
        self.contact_cache = None

    def open_contacts_page(self):
        wd=self.app.wd
        #if wd.current_url.endswith("edit.php") or wd.current_url != "http://localhost/addressbook/":
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd=self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox']").click()
        #wd.find_element_by_xpath("//input[@name='selected[]'][@type='checkbox'][@title='Select (" + firstname + " " + lastname + ")']").click()
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_index(self,index):
        wd=self.app.wd
        self.open_contacts_page()
        contacts=wd.find_elements_by_xpath("//input[@name='selected[]'][@type='checkbox']")
        contacts[index].click()
        wd.find_element_by_xpath("//input[@type='button'][@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

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
        self.change_field_value("notes", contact.notes)

    def submit_contact_form(self):
        wd = self.app.wd
        if 'id=' in wd.current_url:
            wd.find_element_by_xpath("//input[@name='update'][@value='Update']").click()
        else:
            wd.find_element_by_xpath("//input[@name='submit'][@value='Enter']").click()
        wd.find_element_by_link_text("home").click()


    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                firstname=cells[2].text
                lastname=cells[1].text
                all_phones=cells[5].text
                address = cells[3].text
                emails = cells[4].text.splitlines()
                email = emails[0]
                email2 = emails[1]
                homepage = cells[9].find_element_by_tag_name("a").get_attribute("href")
                contact_id=element.find_element_by_tag_name("input").get_attribute("id")
                self.contact_cache.append(Contact(id=contact_id,firstname=firstname,lastname=lastname,all_phones_from_home_page=all_phones,address=address,email=email,email2=email2,homepage=homepage))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd=self.app.wd
        self.app.open_home_page()
        row=wd.find_elements_by_name("entry")[index]
        cell=row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        homephone2 = wd.find_element_by_name("phone2").get_attribute("value")
        cellphone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        homepage = wd.find_element_by_name("homepage").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname,lastname=lastname,id=id,
                       homephone=homephone,homephone2=homephone2,
                       cellphone=cellphone,workphone=workphone, email=email,email2=email2,address=address,homepage=homepage)

    def contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone=re.search("H: (.*)", text).group(1)
        cellphone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        homephone2 = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, homephone2=homephone2,
                       cellphone=cellphone, workphone=workphone)