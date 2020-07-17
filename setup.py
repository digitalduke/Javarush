import os

from setuptools import (
    find_packages,
    setup,
)


with open(
    os.path.join(os.path.dirname(__file__), 'README.md'),
    encoding='utf8'
) as readme_file:
    long_description = readme_file.read()

setup(
    name='nnst',
    version='0.0.1',
    author='George P.',
    author_email='digitalduke@pm.me',
    description='simple calc for NNST',
    entry_points={
        'console_scripts': [
            'nnst=nnst.cli:cli',
        ],
    },
    long_description=long_description,
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
