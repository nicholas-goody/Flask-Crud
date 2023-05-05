from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'some_random_data'

@app.route('/')
def Index():
    return render_template('index.html')