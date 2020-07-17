import os
from pathlib import Path
from sys import stderr

import click
from flask import Flask
from nnst.db.db import DbManager
from nnst.handlers import calc


TEST_DATA = Path(__file__).parent / 'db' / 'import.json'


@click.group()
def cli() -> None:
    if not os.path.isfile(TEST_DATA):
        stderr.write('Error: file with fake test does not exists\n')
        exit(1)

    DbManager.setup_db()
    DbManager.fill_db(path=TEST_DATA)


@cli.command()
def serve() -> None:
    app = Flask(__name__)
    app.register_blueprint(calc.blueprint)

    app.run(host='0.0.0.0', port=5000)

    DbManager.drop_db()
