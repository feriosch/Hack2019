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

rows = []
qbfile = open("nophishies.txt", "r")

for URL in qbfile:


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
    print(domain, "domain")

    if(estaEnWhoIs == 1):
        try:
            if(isinstance(domain.creation_date, list)):
                fechaDeCreacion = domain.creation_date[0]
                edad = (ahorita - fechaDeCreacion).days
            elif (domain.creation_date is None):
                edad = -1
            else:
                fechaDeCreacion = domain.creation_date
                edad = (ahorita-fechaDeCreacion).days
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
    print(tieneCert," cert")
    if tieneCert:
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        holea = x509.get_subject().get_components()
        issuer = x509.get_issuer()
        issued_by = issuer.CN
        print(issued_by)

    rango = -1
    try:
        sopa = bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ result),features="html.parser")
        rango = sopa.reach['rank']
    except:
        pass
    print(rango)

    rows.append([result,esIP,longitud,tieneArroba,tieneGuion,numeroDePuntos,tieneHTTPS,estaEnWhoIs,edad,DNSRecord,issued_by,rango])


qbfile.close()
with open("NoPhishData.csv", 'a') as csvFile:

    for row in rows:
        writer = csv.writer(csvFile)
        writer.writerow(row)

csvFile.close()