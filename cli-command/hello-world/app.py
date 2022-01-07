import click
from flask import Flask

app = Flask(__name__)


@app.cli.command("hello")
@click.argument("name", required=False)
def hello(name):
    if name is None:
        print("Hello World!")
    else:
        print("Hello " + name)
