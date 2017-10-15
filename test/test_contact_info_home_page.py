from random import randrange
import re

def test_contact_info_home_page(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #compare phones
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    #compare emails
    contact_from_edit_page.all_emails = "\n".join([contact_from_edit_page.email,contact_from_edit_page.email2])
    assert contact_from_edit_page.all_emails == contact_from_home_page.all_emails_from_home_page
    #compare address
    assert contact_from_home_page.address ==contact_from_edit_page.address
    #compare FIO
    assert contact_from_edit_page == contact_from_home_page


def clear(s):
    return re.sub("[-() ]","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone,contact.cellphone,contact.workphone,contact.homephone2]))))