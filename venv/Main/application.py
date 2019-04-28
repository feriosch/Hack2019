from flask import Flask,render_template,request, redirect, url_for, request,json, jsonify
from flask_pymongo import PyMongo
import urllib3, requests, json
import re
import whois
import socket
from urllib.parse import urlparse
import datetime
import OpenSSL
import urllib, bs4
import socket
from urllib.request import urlopen
import ssl
import csv
import json as JSON
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

app = Flask(__name__)
app.secret_key = "ElPatatita"





@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

@app.route('/signUp')
def signUp():
    return render_template('pitero.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['user']
    password = request.form['pass']
    return jsonify({'status':'OK','user':user,'pass':password})

@app.route('/validar', methods=['POST'])
def validar():
    # retrieve your wml_service_credentials_username, wml_service_credentials_password, and wml_service_credentials_url from the
    # Service credentials associated with your IBM Cloud Watson Machine Learning Service instance

    wml_credentials={
    "url": "https://us-south.ml.cloud.ibm.com",
    "username": "7e70c510-1ff2-4ec1-9de8-acfdce195ee1",
    "password": "a84e9349-da3c-449c-82af-570bd01c2f41"
    }

    headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'], password=wml_credentials['password']))
    url = '{}/v3/identity/token'.format(wml_credentials['url'])
    response = requests.get(url, headers=headers)
    mltoken = json.loads(response.text).get('token')

    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"fields": ["Domain", "IP", "longitud", "arroba", "guion", "puntos", "HTTPS", "whoIs", "edad", "DNS", "issued", "rango"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/0b8a2b9e-7d85-4dfc-8918-bfd6701f2eca/deployments/2b8e5908-cdb3-4485-95e1-f926f968254d/online', json=payload_scoring, headers=header)
    print("Scoring response")
    print(json.loads(response_scoring.text))
    return("Patata")


@app.route('/validacion', methods=['POST','GET','OPTIONS'])
def validacion():
    if request.method == 'POST':
        print(request.form)
        URL = request.form['url']
        parsed_uri = urlparse(URL)
        result = (parsed_uri.netloc)
        print(result)

        esIP = -1
        try:
            socket.inet_aton(result)
            esIP = 1
        except socket.error:
            pass
        print(esIP)

        longitud = len(URL)
        print(longitud)

        tieneArroba = URL.find("@")
        if tieneArroba >= 0:
            tieneArroba = 1
        print(tieneArroba)

        tieneGuion = URL.find("-")
        if tieneGuion >= 0:
            tieneGuion = 1
        print(tieneGuion)

        numeroDePuntos = URL.count(".")
        print(numeroDePuntos)

        tieneHTTPS = URL.find("https://")
        if tieneHTTPS >= 0:
            tieneHTTPS = 1
        print(tieneHTTPS)

        estaEnWhoIs = 1
        try:
            domain = whois.whois(result)
        except:
            estaEnWhoIs = -1

        print(estaEnWhoIs)

        edad = -1
        ahorita = datetime.datetime.now()

        if (estaEnWhoIs == 1):
            try:
                if (isinstance(domain.creation_date, list)):
                    fechaDeCreacion = domain.creation_date[0]
                    edad = (ahorita - fechaDeCreacion).days
                elif (domain.creation_date is None):
                    edad = -1
                else:
                    fechaDeCreacion = domain.creation_date
                    edad = (ahorita - fechaDeCreacion).days
            except:
                pass
        print(edad)

        parsed_uri = urlparse(URL)
        result = (parsed_uri.netloc)

        DNSRecord = 1
        try:
            u = socket.gethostbyname(result)
        except socket.error:
            DNSRecord = -1
        print(DNSRecord)

        tieneCert = True

        issued_by = ""

        try:
            cert = (ssl.get_server_certificate((result, 443)))
        except:
            tieneCert = False
        print(tieneCert, " cert")
        if tieneCert:
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            holea = x509.get_subject().get_components()
            issuer = x509.get_issuer()
            issued_by = issuer.CN
            print(issued_by)

        rango = -1
        try:
            sopa = bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + result),
                                     features="html.parser")
            rango = sopa.reach['rank']
        except:
            pass
        print(rango)

        wml_credentials = {
            "url": "https://us-south.ml.cloud.ibm.com",
            "username": "7e70c510-1ff2-4ec1-9de8-acfdce195ee1",
            "password": "a84e9349-da3c-449c-82af-570bd01c2f41"
        }

        print("Mi amor")
        valores = [result, esIP, longitud, tieneArroba, tieneGuion, numeroDePuntos, tieneHTTPS, estaEnWhoIs, edad,
                   DNSRecord,
                   issued_by, int(rango)]
        valorsotes = []
        valorsotes.append(valores)
        print(valores)
        headers = urllib3.util.make_headers(
            basic_auth='{username}:{password}'.format(username=wml_credentials['username'],
                                                      password=wml_credentials['password']))
        url = '{}/v3/identity/token'.format(wml_credentials['url'])
        response = requests.get(url, headers=headers)
        mltoken = json.loads(response.text).get('token')

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {
            "fields": ["Domain", "IP", "longitud", "arroba", "guion", "puntos", "HTTPS", "whoIs", "edad", "DNS",
                       "issued",
                       "rango"],
            "values": valorsotes}

        response_scoring = requests.post(
            'https://us-south.ml.cloud.ibm.com/v3/wml_instances/0b8a2b9e-7d85-4dfc-8918-bfd6701f2eca/deployments/2b8e5908-cdb3-4485-95e1-f926f968254d/online',
            json=payload_scoring, headers=header)
        print("Scoring response")
        resultado = json.loads(response_scoring.text)
        print(resultado)
        print("DEbug")
        veredicto = resultado['values'][0][16]
        print(resultado['values'][0][16])
        print("json")
        print("Gola")
        print(type(jsonify({'status': 'OK', 'vered': veredicto})))

        return jsonify(status = 'OK', vered= veredicto)
    else:
        return render_template('validacion.html')