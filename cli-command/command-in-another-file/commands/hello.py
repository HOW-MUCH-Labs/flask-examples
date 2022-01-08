from flask import Flask
from flask import Blueprint
import click


app = Flask(__name__)

custom_blueprint = Blueprint('custom', __name__)
# Add short help for the CLI group when listing the commands available to Flask
custom_blueprint.cli.short_help = "My custom commands"


@custom_blueprint.cli.command("hello")
@click.argument("name", required=False)
def hello(name):
    """ Say hello to the personam named with {name} """
    if name is None:
        print("Hello World!")
    else:
        print("Hello " + name)