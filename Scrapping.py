import urllib.request
from bs4 import BeautifulSoup
import pandas
cucei = "http://cucei.udg.mx/directorio"
#cucei="file:///C:/Users/Arturo/Desktop/Directorio.html"

page = urllib.request.urlopen(cucei)
soup = BeautifulSoup(page)


def cutit(s,n):    
   return s[n:]


items = soup.find_all('div', class_="item-list") 
print(items[0].h3.string)
print(items[0].ul.li.a.string)

items_puesto=soup.find("div", class_="puesto-directorio").findAll()
for i in items_puesto:
	puesto = i.next_sibling
print(puesto)

for i in soup.find("div", class_="direccion-directorio").findAll():
	direccion = i.nextSibling
print(direccion)

for i in soup.find("div", class_="views-field-field-conmutador").findAll():
	conmutador = i.nextSibling
print(conmutador)


print("")
print("")

#itemsPuesto = soup.find_all('div', class_="puesto-directorio")
#print(itemsPuesto[1].nextSibling)  
#itemsDireccion = soup.find_all('div', class_="direccion-directorio")
#print(itemsDireccion[0].div.text)
#itemsTelefono = soup.find_all('div', class_="views-field-field-conmutador")
#print(itemsTelefono[0].div.text)










#for x in items:
#	print(x.h3.string, " - ", x.ul.li.a.string)


