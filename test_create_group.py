# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_group(app):
    app.login(username="admin",password="secret")
    app.create_group(Group(name= "new_group",header= "header_text",footer= "footer_text"))
    app.logout()


def test_create_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

