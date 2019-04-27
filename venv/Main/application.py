from flask import Flask,render_template,request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "ElPatatita"

def Patitos():
    pass

@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
        request.form.get("palabra_clave")


