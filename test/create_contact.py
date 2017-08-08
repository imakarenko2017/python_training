# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.open_contact_form()
    app.contact.fill_contact_form(Contact(firstname="Inna",middlename="I",lastname="Makarenko",title="Ms",nickname="imakarenko",company="Vintelligent",address="Alton Pl",cellphone="",workphone="",email="",email2="",email3="",homepage="",anniversary="",birthday="1",birthmonth="January",birthyear="1980",homephone2="",address2="",homephone="123123123",notes="test contact"))
    app.contact.submit_contact_form()
    app.session.logout()


