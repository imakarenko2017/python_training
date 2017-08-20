
from model.contact import Contact


def test_delete_contact (app):
    firstname="Inessa"
    lastname="Molchanova"
    if not app.contact.is_exist(firstname,lastname):
        app.contact.create(Contact(firstname="Inessa",lastname="Molchanova"))
    app.contact.delete(firstname="Inessa",lastname="Molchanova")


