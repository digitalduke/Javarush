from typing import List

from cian_core.settings.base import *  # pylint: disable=wildcard-import,unused-wildcard-import


APPLICATION_NAME = '{{ cookiecutter.microservice_name }}'
APPLICATION_DESCRIPTION = '{{ cookiecutter.short_description }}'
APPLICATION_PACKAGE_NAME = '{{ cookiecutter.python_package_name }}'

CHECK_SERVICES: List[str] = []
