import pytest
from tornado import web

from {{ cookiecutter.python_package_name }}.web.urls import urlpatterns


@pytest.fixture
def app():
    return web.Application(urlpatterns)
