
from model.contact import Contact


def test_delete_contact (app):
    app.session.login(username="admin",password="secret")
    app.contact.delete(Contact("Inessa","I","Molchanova","","","","","","","","","","","","","","","","","",""))
    app.session.logout()