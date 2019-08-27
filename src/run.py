#!/usr/bin/env python3
__author__ = "Paul Schifferer <paul@schifferers.net>"


from app import app
import argparse


parser = argparse.ArgumentParser()
parser.add_argument(
    "--bind",
    "-b",
    help="address to bind to",
    type=str,
    default="0.0.0.0",
    action="store",
)
parser.add_argument(
    "--port", "-p", help="port number", type=int, default=5000, action="store"
)
parser.add_argument(
    "--debug", help="Enable debug mode", action="store_true", default=False
)
args = parser.parse_args()

app.run(host=args.bind, port=args.port, debug=args.debug)
