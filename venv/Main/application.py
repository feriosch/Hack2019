from flask import Flask,render_template,request, redirect, url_for, request,json, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "ElPatatita"



@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
        if request.form["btn"] == "URL":
            request.form.get("url")
        if request.form["btn"] == "correo":
            request.join
    else:
        return render_template('pitero.html')

@app.route('/signUp')
def signUp():
    return render_template('pitero.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['user']
    password = request.form['pass']
    return jsonify({'status':'OK','user':user,'pass':password})
