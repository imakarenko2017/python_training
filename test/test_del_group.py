from model.group import Group
from random import randrange

def test_delete_first_group(app):
    app.session.login()
    app.group.delete_group_by_index(0)
    app.session.logout()




def test_delete_some_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test",header="hh"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups=app.group.get_group_list()
    assert len(old_groups)-1==len(new_groups)
    old_groups[index:index+1]=[]
    assert old_groups == new_groups
