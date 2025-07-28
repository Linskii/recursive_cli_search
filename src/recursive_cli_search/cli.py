import click


@click.command()
@click.argument("searchword")
@click.argument("commandname")
def cli(searchword, commandname):
    pass


if __name__ == "__main__":
    cli()
