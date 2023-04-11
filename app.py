from flask import Flask, render_template, request
import pandas as pd
from scipy.spatial.distance import cosine, euclidean, hamming
from flask_table import Table, Col

class Results(Table):
    id = Col('id', show=False)
    title = Col('name')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")