# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(maxlen):
    symbols = string.ascii_letters+string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen):
    symbols = string.ascii_letters+string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@mail.ru"
def random_homepage():
    symbols = string.ascii_letters+string.digits
    return "http://" + "".join(random.choice(symbols)+ "." + "com")


testdata = [Contact(firstname="", lastname="", middlename="")]+ [
    Contact(firstname=random_string(10), lastname=random_string(10),
            middlename=random_string(5), company=random_string(10),
            email=random_email(6),email2=random_email(7),homepage= random_homepage())
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app,contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    new_contacts=app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)+1
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)


