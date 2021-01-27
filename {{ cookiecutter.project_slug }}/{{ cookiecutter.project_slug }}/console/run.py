import click


@click.command()
@click.argument("person")
def cli(person):
    """Say hello to a person"""

    click.echo(f"Hello, {person}")
