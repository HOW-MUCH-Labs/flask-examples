from flask import Flask
from commands.hello import custom_blueprint

app = Flask(__name__)

# you MUST register the blueprint
app.register_blueprint(custom_blueprint)