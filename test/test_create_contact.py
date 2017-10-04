# -*- coding: utf-8 -*-
from model.contact import Contact

def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    #print(len(old_contacts))
    #print(old_contacts)
    contact=Contact(firstname="Vasiliy",middlename="I",lastname="Noname",title="Ms",nickname="vasya",company="Vintelligent",address="Alton Pl",cellphone="",workphone="",email="",email2="",email3="",homepage="",anniversary="",birthday="1",birthmonth="January",birthyear="1980",homephone2="",address2="",homephone="123123123",notes="test contact")
    app.contact.create(contact)
    new_contacts=app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)+1
    #print(len(new_contacts))



