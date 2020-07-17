import click


@click.group()
def cli() -> None:
    pass


@cli.command()
def serve() -> None:
    pass
