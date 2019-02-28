#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "My first flask application !"

app.run()
