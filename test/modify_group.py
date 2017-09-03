
from model.group import Group


def test_modify_groupname(app):
    old_groups = app.group.get_group_list()
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", header="hh"))
    app.group.modify_first_group(Group(name="Group_0814"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

def test_modify_groupheader(app):
    old_groups = app.group.get_group_list()
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", header="hh"))
    app.group.modify_first_group(Group(header="hh"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_groupfooter(app):
    old_groups = app.group.get_group_list()
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", footer="Footer 0814"))
    app.group.modify_first_group(Group(footer="Footer 0814"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
