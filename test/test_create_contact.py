# -*- coding: utf-8 -*-
from model.contact import Contact

def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact=Contact(firstname="Anna",middlename="I",lastname="Petrova",title="Ms",nickname="Petrova",company="Coca-Cola",address="Alton Pl",cellphone="",workphone="",email="",email2="",email3="",homepage="",anniversary="",birthday="1",birthmonth="January",birthyear="1980",homephone2="",address2="",homephone="123123123",notes="test contact")
    app.contact.create(contact)
    new_contacts=app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)+1
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)


