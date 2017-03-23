import urllib.request
from bs4 import BeautifulSoup
import pandas
#cucei = "http://cucei.udg.mx/directorio"
cucei="file:///C:/Users/Arturo/Desktop/Directorio.html"

page = urllib.request.urlopen(cucei)
soup = BeautifulSoup(page)

puestogeneral = []
nombre = []
items = soup.find_all('div', class_="item-list") 
for i in items:
	puestogeneral.append(i.h3.string)
	nombre.append(i.ul.li.a.string)

print(nombre[0].string)
print(puestogeneral[0].string)

puesto =[] 
listaPuestos = soup.find_all(class_="puesto-directorio")
for i in listaPuestos:
    if i.strong == None or i.strong == " ":
    	puesto.append("Sin valor")
    else:
        puesto.append(i.strong.nextSibling)

direccion = []
listaDireccion = soup.find_all(class_="direccion-directorio")
for i in listaDireccion:
	if i.strong == None or i.strong == " ":
		direccion.append("Sin valor")
	else:
		direccion.append(i.strong.nextSibling)

telefono = []
listaTelefonos = soup.find_all(class_="telefono-directorio")
for i in listaTelefonos:
	if i.strong == None or i.strong == " ":
		telefono.append("Sin valor")
	else:
		telefono.append(i.strong.nextSibling)

conmutador = []
listaConmutador = soup.find_all(class_="views-field-field-conmutador")
for i in listaConmutador:
	if i.strong == None or i.strong == " ":
		conmutador.append("Sin valor")
	else:
		conmutador.append(i.strong.nextSibling)


fax = []
listaFax = soup.find_all(class_="views-field-field-fax")
for i in listaFax:
	if i.strong == None or i.strong == " ":
		fax.append("Sin valor")
	else:
		fax.append(i.strong.nextSibling)


imagenes = []
listaImagenes = soup.find_all(class_="foto-directorio")
for i in listaImagenes:
	if i.img['src'] != None:
		imagenes.append(i.img['src'])

fax = []
listaFax = soup.find_all(class_="views-field-field-fax")
for i in listaFax:
	if i.strong == None or i.strong == " ":
		fax.append("Sin valor")
	else:
		fax.append(i.strong.nextSibling)



print(len(puestogeneral))
print(len(nombre))
print(len(puesto))
print(len(direccion))
print(len(conmutador)) 
print(len(imagenes))

df = pandas.DataFrame(puestogeneral, columns=['Puesto General'])
df['Titular']=nombre
df['Puesto']=puesto
df['Dirección']=direccion
df['Teléfono']=telefono
df['Conmutador']=conmutador
df['Fax']=fax
df['Imágenes']=imagenes
salida=open('cucei.html', 'w')
#salida.write('<meta charset ="UTF-8">')
salida.write(df.to_html())
salida.close()
