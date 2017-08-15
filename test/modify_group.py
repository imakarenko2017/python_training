
from model.group import Group


def test_modify_groupname(app):
    app.group.modify_first_group(Group(name="Group_0814"))

def test_modify_groupheader(app):
    app.group.modify_first_group(Group(header="Header_0814"))
    app.session.logout()

def test_modify_groupfooter(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(footer="Footer 0814"))
    app.session.logout()
