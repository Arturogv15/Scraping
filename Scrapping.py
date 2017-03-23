import urllib.request
from bs4 import BeautifulSoup
import pandas
cucei = "http://cucei.udg.mx/directorio"
#cucei="file:///C:/Users/Arturo/Desktop/Directorio.html"

page = urllib.request.urlopen(cucei)
soup = BeautifulSoup(page)

items = soup.find_all('div', class_="item-list") 
print(items[0].h3.string)
print(items[0].ul.li.a.string)

puesto =[] 
listaPuestos = soup.find_all(class_="puesto-directorio")
for i in listaPuestos:
    if i.strong != None:
        puesto.append(i.strong.nextSibling)

direccion = []
listaDireccion = soup.find_all(class_="direccion-directorio")
for i in listaDireccion:
	if i.strong != None:
		direccion.append(i.strong.nextSibling)

conmutador = []
listaConmutador = soup.find_all(class_="views-field-field-conmutador")
for i in listaConmutador:
	if i.strong != None:
		conmutador.append(i.strong.nextSibling)

imagenes = []
listaImagenes = soup.find_all(class_="foto-directorio")
for i in listaImagenes:
	if i.img.src != None:
		imagenes.append(i.img.src.string)

print(imagenes[1])
