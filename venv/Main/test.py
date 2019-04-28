import re
import whois
import socket
from urllib.parse import urlparse
import datetime

URL = "https://mimamamemima-guapo.com.mx"
URL2 = "http://125.32.25.23/banorte/depositar"
URL3 = "https://www.google.com/"
#URL3 = "https://nerantzis.gr/administrator/components/com_checkin/-/www.bancobrasil.com.br/Confirmacao/Obrigatoria/Procedimento/Seguro/?GisPvDj8KG=phishing@fraude.com.br%20%20&PDdE4zssDw=&oJvT2T7RQr=9318629"

parsed_uri = urlparse(URL3)
result = (parsed_uri.netloc)
print(result)

longitud = len(URL3)
print(longitud)

tieneArroba = URL3.find("@")
if tieneArroba >= 0:
    tieneArroba = 1
print(tieneArroba)

tieneGuion = URL3.find("-")
if tieneGuion >= 0:
    tieneGuion = 1
print(tieneGuion)

numeroDePuntos = URL3.count(".")
print(numeroDePuntos)

tieneHTTPS = URL3.find("https://")
if tieneHTTPS >= 0:
    tieneHTTPS = 1
print(tieneHTTPS)

estaEnWhoIs = 1
try:
    domain = whois.whois(URL3)
except:
    estaEnWhoIs = -1

print(estaEnWhoIs)

edad = -1
ahorita = datetime.datetime.now()
if(estaEnWhoIs == 1):
    fechaDeCreacion = domain.creation_date[0]
    edad = (ahorita-fechaDeCreacion).days



parsed_uri = urlparse(URL3)
result = (parsed_uri.netloc)


DNSRecord = 1
try:
    u = socket.gethostbyname(result)
except socket.error:
    DNSRecord = -1
print(DNSRecord)




