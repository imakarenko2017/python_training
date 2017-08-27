
from model.group import Group


def test_modify_groupname(app):
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", header="hh"))
    app.group.modify_first_group(Group(name="Group_0814"))

def test_modify_groupheader(app):
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", header="hh"))
    app.group.modify_first_group(Group(header="hh"))

def test_modify_groupfooter(app):
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", footer="Footer 0814"))
    app.group.modify_first_group(Group(footer="Footer 0814"))
