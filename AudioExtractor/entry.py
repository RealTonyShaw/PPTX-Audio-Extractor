import click


@click.command()
def hello():
    click.echo('hello world')


@click.command()
@click.option('--talk', help='print a simple string')
def talk():
    click.echo('hello')


if __name__ == '__main__':
    hello()
    talk()