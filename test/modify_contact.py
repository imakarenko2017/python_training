
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count()==0:
       app.contact.create(Contact(firstname="Inessa",middlename="I",lastname="Molchanova",birthday="3",birthmonth="March",birthyear="1980",email="inna.makarenko@gmail.com"))
    app.contact.modify_first_contact(Contact(firstname="Updated Name",lastname="Updated Lastname"))