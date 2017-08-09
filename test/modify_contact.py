
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.modify(Contact("Inessa","I","Molchanova","","","","","","","","","","","","","","","","","",""))
    app.session.logout()