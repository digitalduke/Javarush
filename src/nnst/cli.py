import click
from flask import Flask
from nnst.handlers import calc


@click.group()
def cli() -> None:
    pass


@cli.command()
def serve() -> None:
    app = Flask(__name__)
    app.register_blueprint(calc.blueprint)

    app.run(host='0.0.0.0', port=5000)
