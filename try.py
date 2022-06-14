import datetime
from datetime import date, time, datetime
import pandas as pd

archiveStock = "Base de datos de stock.xlsx"
archive = pd.read_excel(archiveStock)
codia=archive[archive["code"]==30].index
print(codia)
dele=archive.drop(codia)
print(dele)

##d_index = archive.to_dict('index')
#print(d_index)
#Sirve para filtrar el contenido de una columna
#archive = archive["price"] 

#Fitrar varias columnas
#archive = archive[["code", "product", "price"]]

#Filtrar por filas (con solo un indice me muestra una sola fila, con 2 indices me muestra hasta la anterior
# del máximo)
#archive = archive.iloc[0:3]
#Filtrar por contenido por fila pero eligiendola
#archive = archive.iloc[[0,5,2]]

#Filtrar por contenido en la primera fila
#archive = archive.loc[[0,5,4]]

#Filtrar por filas y columnas
#archive = archive.loc[[0,5,4] , ["code", "product"]]

#Filtrar por condición de una columna
#archive = archive[archive["product"]=="Alfajor Fantoche"]

#Filtrar por el nombre del producto
#introduceCode = str(input("Escribe el nombre de un producto"))
#archive = archive[archive["product"]==str(introduceCode)]

#Filtrar por producto
#introduceCode = str(input("Escribe el código de un producto"))
#archive = archive[archive["product"]==str(introduceCode)]
#line = int(input("Escriba el número de la fila que desea filtrar"))
#archive = archive.iloc[int(line)]
# column = str(input("Escribe el nombre de la columna que deseas filtrar"))
# archive = archive[column]
# #def calculatorBenefit ():
#     #moneyBenefit = ("price" - "cost") * "cant sells"
#     #print(moneyBenefit)

# print(archive)