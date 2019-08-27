__author__ = "Paul Schifferer <paul@schifferers.net>"

# Import flask and template operators
from flask import Flask, render_template

# from flask_locale import Locale, _
import logging
from app.common import constants
import os


# Import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object("config")

logging.basicConfig(level=(logging.INFO if not app.debug else logging.DEBUG))


# Define the database object which is imported
# by modules and controllers
# db = SQLAlchemy(app)
# db = boto3.client('dynamodb')
from pymongo import MongoClient

mongo_client = MongoClient(os.environ[constants.MONGODB_URL_ENV])
db = mongo_client.mellon

# Locale
# locale = Locale(app)

# Sentry
import sentry_sdk

sentry_sdk.init(os.environ[constants.SENTRY_DSN_ENV])

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.core.controllers import core as core_module
from app.mod_discord.controllers import discord as discord_module
from app.mod_slack.controllers import slack as slack_module

# Register blueprint(s)
print("Registering application module blueprints...")
app.register_blueprint(core_module)
app.register_blueprint(discord_module)
app.register_blueprint(slack_module)

from app.core import setup

setup.initialize()
