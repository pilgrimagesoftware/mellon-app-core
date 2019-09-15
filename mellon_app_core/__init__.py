__author__ = "Paul Schifferer <paul@schifferers.net>"

# Import flask and template operators
# from flask import Flask, render_template, jsonify, g

# # from flask_locale import Locale, _
# import logging
# import os
# from mellon_common import constants, exceptions
# import sentry_sdk
# from sentry_sdk.integrations.flask import FlaskIntegration
# from prometheus_flask_exporter import PrometheusMetrics
# import dotenv


# # def create_app(app_name: str, blueprint_modules: list, env_path: str=os.path.join(os.path.dirname(__file__), '.env')):
# def create_app():
#     # Define the WSGI application object
#     app = Flask(__name__)

#     # Import SQLAlchemy
#     # from flask.ext.sqlalchemy import SQLAlchemy

#     # Configurations
#     # app.config.from_object("config")
#     print(f"env_path={env_path}")
#     dotenv.load_dotenv(env_path)
#     # TODO: configure from .env
#     print(f"env={os.environ}")

#     # logging.basicConfig(level=(logging.INFO if not app.debug else logging.DEBUG))

#     # Sentry
#     sentry_sdk.init(os.environ[constants.SENTRY_DSN_ENV], integrations=[FlaskIntegration()])

#     # Define the database object which is imported
#     # by modules and controllers
#     # db = SQLAlchemy(app)
#     # db = boto3.client('dynamodb')
#     # from pymongo import MongoClient

#     # mongo_client = MongoClient(os.environ[constants.MONGODB_URL_ENV])
#     # db = mongo_client.mellon

#     # Locale
#     # locale = Locale(app)

#     # TODO: Setup Prometheus metrics endpoint
#     # metrics = PrometheusMetrics(app)
#     # metrics.info("app_info", "Application info", version="0.0.1")
#     # g["metrics"] = metrics

#     # Import a module / component using its blueprint handler variable
#     # import mellon_core_module
#     # import mellon_slack_module

#     # import mellon_discord_module

#     # Register blueprint(s)
#     app.logger.info("Registering application module blueprints...")
#     for bp in blueprint_modules:
#         app.logger.debug(f"Blueprint: {bp}")
#         app.register_blueprint(bp)
#     # app.register_blueprint(discord_module)
#     # app.register_blueprint(mellon_slack_module.blueprint)

#     # from app.core import setup

#     # setup.initialize()

#     @app.errorhandler(exceptions.APIException)
#     def handle_invalid_usage(error):
#         response = jsonify(error.to_dict())
#         response.status_code = error.status_code
#         return response

#     return app
