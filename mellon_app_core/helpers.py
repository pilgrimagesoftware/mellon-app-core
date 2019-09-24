__author__ = "Paul Schifferer <paul@schifferers.net>"

import os
import dotenv
import sentry_sdk
from flask import jsonify
from sentry_sdk.integrations.flask import FlaskIntegration
from prometheus_flask_exporter import PrometheusMetrics
from mellon_common import constants, exceptions


def setup_app(app, env_path: str, blueprint_modules: list):
    app.logger.debug(f"env_path={env_path}; blueprint_modules={blueprint_modules}")

    # Sentry
    sentry_dsn = os.environ[constants.SENTRY_DSN_ENV]
    app.logger.debug(f"sentry_dsn={sentry_dsn}")
    sentry_sdk.init(sentry_dsn, integrations=[FlaskIntegration()])

    # Import SQLAlchemy
    # from flask.ext.sqlalchemy import SQLAlchemy

    # Configurations
    # app.config.from_object("config")
    # print(f"env_path={env_path}")
    dotenv.load_dotenv(env_path)
    # TODO: configure from .env
    # print(f"env={os.environ}")

    # logging.basicConfig(level=(logging.INFO if not app.debug else logging.DEBUG))

    # Sentry
    # sentry_sdk.init(os.environ[constants.SENTRY_DSN_ENV], integrations=[FlaskIntegration()])

    # Define the database object which is imported
    # by modules and controllers
    # db = SQLAlchemy(app)
    # db = boto3.client('dynamodb')
    # from pymongo import MongoClient

    # mongo_client = MongoClient(os.environ[constants.MONGODB_URL_ENV])
    # db = mongo_client.mellon

    # Locale
    # locale = Locale(app)

    # TODO: Setup Prometheus metrics endpoint
    metrics = PrometheusMetrics(app)
    metrics.info("app_info", "Application info", version="0.0.1")
    # g["metrics"] = metrics

    # Register blueprint(s)
    app.logger.info("Registering application module blueprints...")
    for bp in blueprint_modules:
        app.logger.debug(f"Blueprint: {bp}")
        app.register_blueprint(bp)

    @app.errorhandler(exceptions.APIException)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
