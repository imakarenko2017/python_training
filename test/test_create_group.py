# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    app.group.create(Group(name="new_group", header="header_text", footer="footer_text"))


def test_create_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


