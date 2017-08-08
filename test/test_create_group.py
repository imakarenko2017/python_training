# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    app.session.login(username="admin",password="secret")
    app.group.create(Group(name="new_group", header="header_text", footer="footer_text"))
    app.session.logout()


def test_create_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

