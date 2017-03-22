import urllib.request
from bs4 import BeautifulSoup
import pandas
cucei = "http://cucei.udg.mx/directorio"
#cucei="file:///C:/Users/Arturo/Desktop/Directorio.html"

page = urllib.request.urlopen(cucei)

soup = BeautifulSoup(page)

#soup.title.string 

def cutit(s,n):    
   return s[n:]


items = soup.find_all('div', class_="item-list") 
print(items[0].h3.string)
print(items[0].ul.li.a.string)

items2=[]
for n in items:
	items_puesto=soup.find("div", class_="puesto-directorio").findAll()
	for i in items_puesto:
		puesto = i.next_sibling
	print(puesto)

#items2[n].append(puesto)


#for n in range(10):
#	for i in soup.find("div", class_="puesto-directorio").findAll():
#		puesto = i.nextSibling
#	items_puesto[n] = ''.join(puesto)
#		#items_puesto[n]=puesto

#print(items2[0])


#print(items_puesto)
for i in soup.find("div", class_="direccion-directorio").findAll():
	direccion = i.nextSibling
print(direccion)

for i in soup.find("div", class_="views-field-field-conmutador").findAll():
	conmutador = i.nextSibling
print(conmutador)


#for i in soup.find('div', class_="views-field-field-correo-electronico").findAll():
#	correo = i.nextSibling
#print(correo)

print("")
print("")

#itemsPuesto = soup.find_all('div', class_="puesto-directorio")
#print(itemsPuesto[1].nextSibling)  
#itemsDireccion = soup.find_all('div', class_="direccion-directorio")
#print(itemsDireccion[0].div.text)
#itemsTelefono = soup.find_all('div', class_="views-field-field-conmutador")
#print(itemsTelefono[0].div.text)
#itemsCorreo = soup.find_all('span', id_="6a1ccbef6ebe9d6e42f41b7f2bb6a80302c2d804")
#itemsCorreo = soup.find_all('div', class_="views-field-field-correo-electronico")
#print(itemsCorreo[0].text) 

#one = soup.find_all("span", {"id": "6a1ccbef6ebe9d6e42f41b7f2bb6a80302c2d804"})
#print(one[0].text) 









#for x in items:
#	print(x.h3.string, " - ", x.ul.li.a.string)


