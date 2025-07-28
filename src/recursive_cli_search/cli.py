import click


@click.command()
@click.argument("search")
@click.argument("command")
def cli(search, command):
    print(f"{search} and {command}")


if __name__ == "__main__":
    cli()
