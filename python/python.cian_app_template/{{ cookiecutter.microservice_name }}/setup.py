import os

from setuptools import find_packages, setup


setup(
    name='{{ cookiecutter.microservice_name }}',
    version='0.1.0',
    author='Cian Team',
    author_email='python@cian.ru',
    description='{{ cookiecutter.short_description }}',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.microservice_name }}={{ cookiecutter.python_package_name }}.cli:cli',
        ],
    },
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)