import click
from modifier import extract_from


@click.command()
@click.option('--path', type=str, help='The path of your .pptx file')
def extract(path):
    extract_from(path)


if __name__ == '__main__':
   extract()