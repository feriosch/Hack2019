import OpenSSL
import urllib, bs4
import socket
from urllib.request import urlopen
import ssl


cert = (ssl.get_server_certificate(('bimbo.com', 443)))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
holea = x509.get_subject().get_components()
issuer = x509.get_issuer()
issued_by = issuer.CN
print(issued_by)
rango = -1
try:
    sopa = bs4.BeautifulSoup(urlopen("http://data.alexa.com/data?cli=10&dat=s&url="+ "hi5.com"),features="html.parser")
    rango = sopa.reach['rank']
except:
    pass
print(rango)

import socket
