
from model.group import Group
from random import randrange


def test_modify_groupname(app):
    if app.group.count()==0:
        app.group.create(Group(name="Group_0814", header="hh"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group=Group(index)
    group.id =old_groups[index].id
    app.group.modify_group_by_index(index,group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_groupheader(app):
#    old_groups = app.group.get_group_list()
    #    if app.group.count()==0:
    #    app.group.create(Group(name="Group_0814", header="hh"))
    #    app.group.modify_first_group(Group(header="hh"))
    #new_groups = app.group.get_group_list()
#assert len(old_groups) == len(new_groups)

#def test_modify_groupfooter(app):
    #   old_groups = app.group.get_group_list()
    #if app.group.count()==0:
    #   app.group.create(Group(name="Group_0814", footer="Footer 0814"))
    #app.group.modify_first_group(Group(footer="Footer 0814"))
    #new_groups = app.group.get_group_list()
#assert len(old_groups) == len(new_groups)
