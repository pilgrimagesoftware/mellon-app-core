FROM python:3.7
LABEL maintainer="Paul Schifferer <paul@schifferers.net"

RUN apt-get -q update                   \
    && DEBIAN_FRONTEND=noninteractive   \
    && apt-get -q -y install python-pip \
    && apt-get -q clean                 \
    && rm -rf /var/lib/apt/lists/*      \
    && pip install pipenv

RUN mkdir -p /opt/flask-app/

COPY config/flask-app.ini /opt/flask-app
COPY src /opt/flask-app/
RUN ls -lR /opt/flask-app

WORKDIR /opt/flask-app
ENV HOME=/opt/flask-app

RUN pipenv install
# RUN ls -lR /opt/flask-app/.local/share/virtualenvs

CMD ["pipenv", "run", "./run.py"]
