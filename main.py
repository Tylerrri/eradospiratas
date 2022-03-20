from flask import Flask, redirect, render_template
from flask import request
import requests
import subprocess
import json
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/loja')
def vips():
    return render_template('loja.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1', debug=True, threaded=True)
