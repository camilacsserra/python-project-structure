import click
from ..resources.ageverifier import ageverifier

@click.command()
def start():
    #click.echo(greetings)
    birth_year = click.prompt("Type you birth year e.g 1999")
    click.echo(ageverifier(birth_year))


start()

    