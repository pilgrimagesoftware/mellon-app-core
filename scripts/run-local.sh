#!/bin/bash

export FLASK_APP=mellon_app:create_app
export FLASK_ENV="development"
export FLASK_DEBUG="True"
export DEBUG="True"
export CSRF_ENABLED="True"
export CSRF_SESSION_KEY="wUP1s5NUwpLHG9xZIdhF6mnlBWNb5VrC"
export SECRET_KEY="gVzHEjBJeazzIccWuyLwTVHxXXDaZpUC"
export SLACK_APP_ID="AMK1GP4Q5"
export SENTRY_DSN="https://d258c5913465433aaa23722909c4ef10@sentry.io/1539488"

pip3 install -r requirements.txt
flask run
