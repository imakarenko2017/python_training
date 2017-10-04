# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    old_groups=app.group.get_group_list()
    group=Group(name="newgroup", header="header_text", footer="footer_text")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1==app.group.count()
    old_groups.append(group)
    assert sorted(old_groups,key=group.id_or_max) == sorted(new_groups,key=group.id_or_max)


def test_create_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups=app.group.get_group_list()
    assert len(old_groups)+1==len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)



