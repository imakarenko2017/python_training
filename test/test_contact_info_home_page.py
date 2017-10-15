from model.contact import Contact
from random import randrange

def test_contact_info_home_page(app):

    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #contact_from_edit_page.all_phones= join
    print(contact_from_home_page.all_phones_from_home_page)
    print (contact_from_edit_page.workphone)
    #print(contact_from_home_page)
    #print(contact_from_edit_page)