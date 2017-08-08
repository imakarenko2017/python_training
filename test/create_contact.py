# -*- coding: utf-8 -*-
from model.contact import Contact

def test_create_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.open_contact_form()
    app.contact.fill_contact_form(Contact(firstname="Inna",middlename="I",lastname="Makarenko",title="Ms",nickname="imakarenko",company="Vintelligent",address="Alton Pl",cellphone="",workphone="",email="",email2="",email3="",homepage="",anniversary="",birthday="1",birthmonth="January",birthyear="1980",homephone2="",address2="",homephone="123123123",notes="test contact"))
    app.contact.submit_contact_form()
    app.session.logout()


