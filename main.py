import click

from Restaurants import Restaurants


@click.group()
def cli():
    """ Simple lunch picker app in python """
    pass


@cli.command()
def pick():
    """ Picks random restaurant from list """
    print(manager.pick())


@cli.command()
@click.argument('restaurant')
def add(restaurant):
    """ Adds restaurant to list to add multiple restaurants use ',' between names """
    manager.add(restaurant)


@cli.command()
@click.argument('restaurant')
def remove(restaurant):
    """ Removes restaurant from list """
    manager.remove(restaurant)


@cli.command()
def show():
    """ Show all restaurants from list """
    print(*manager.show(), sep="\n")


if __name__ == "__main__":
    manager = Restaurants()
    cli()
