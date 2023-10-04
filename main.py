import requests
from bs4 import BeautifulSoup
import re

# Obtener el HTML de la pagina web
url = "https://es.wikipedia.org/wiki/Python"
response = requests.get(url)
html = response.content

# Analizar el HTML utilizando BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Obtener  el titulo de la pagina
title = soup.title.string

print(f"El titulo es: {title}")
print("*" * 100)

# Obtener todos los enlaces de la pagina
links = []
for link in soup.find_all("a", href = True):
    if "http" in link["href"]:
        links.append(link["href"])
print(links)
print("*" * 100)

# Obtener todos los encabezados de la pagina
encabezados = []

for encabezado in soup.find_all(re.compile("^h[1-6]$")):
    encabezados.append(encabezado.text.strip())

print(encabezados)
print("*" * 100)

# Obtener la imagen principal de la pagina
img = soup.find("img", {"class": "mw-file-element"})
img_url = "https:" + img["src"]

print(f"La imagen es: {img_url}")
print("*" * 100)