#primero hacer un menú
from ast import Break, Pass, main
from fileinput import close
import os
import pandas as pd

def wachStock():
    #archiveStock = "Stock.txt"
    #archive = open(archiveStock, "r")
    #content = archive.read()
    #print(content)
    #archive.close()
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print(archive)


def addProduct():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print("Se añadirá un producto")
    #archiveStock = "Stock.txt"
    #archive = open(archiveStock, "w")
    newProduct = {"code":"","product":"","stock":"","cost":"","benefit":"","income":""}
    newProduct["code"] = input("Escribe el código del nuevo producto")
    newProduct["product"] = str(input("Escribe el nombre del producto"))
    newProduct["stock"] = int(input("Escribe la cantidad del producto"))
    newProduct["cost"] = float(input("Escribe cual fue el costo del producto"))
    newProduct["benefit"] = float(input("Escribe cual es el margen de ganancias del producto"))
    newProduct["income"] = float(input("Escribe cual es el precio del producto"))
    archive = archive.append(newProduct, ignore_index=True)
    print(archive)

#def cantFilter():
    #print(numberFilter)
    #archiveStock = "Base de datos de stock.xlsx"
    #archive = pd.read_excel(archiveStock)
    #filterCant = float(input("Escriba el tipo de cantidad que desea filtrar"))
    #if filterCant == 1:
       #cantProduct = int(input("Escribe la cantidad del producto"))
        #archive = archive[archive["cant"]==int(cantProduct)]
        #print(archive)
    #elif filterCant == 2:
        #cantProduct = int(input("Escribe la cantidad del producto"))
        #archive = archive[archive["cant"]>=int(cantProduct)]
        #print(archive)
    #elif filterCant == 3:
        #cantProduct = int(input("Escribe la cantidad del producto"))
        #archive = archive[archive["cant"]<=int(cantProduct)]
        #print(archive)
    #else:
        #print("No eligio ninguna de las opciones posibles")

#def tipeFilter():
    #archiveStock = "Base de datos de stock.xlsx"
    #archive = pd.read_excel(archiveStock)
    #fil = int(input("Escriba el identificador del filtro que desea aplicar"))
    #if fil == 1:
        #introduceCode = int(input("Escribe el código de un producto"))
        #archive = archive[archive["code"]==int(introduceCode)]
        #print(archive)
    #eliif fil == 2:
        #nameProduct = str(input("Escribe el nombre de un producto"))
        #archive = archive[archive["product"]==str(nameProduct)]
        #print(archive)
    #eliif fil == 3:
        #cantFilter()
    #eliif fil == 4:
        #costProduct = float(input("Escribe el costo de un producto"))
        #archive = archive[archive["cost"]==float(costProduct)]
        #print(archive)
    #eliif fil == 5:
        #benefitProduct = float(input("Escribe el beneficio del producto"))
        #archive = archive[archive["benefit"]==float(benefitProduct)]
        #print(archive)
    #eliif fil == 6:
        #priceProduct = float(input("Escribe el beneficio del producto"))
        #archive = archive[archive["price"]==float(benefitProduct)]
        #print(archive)
    #eliif fil == 7:
        #line = int(input("Escriba el número de la fila que desea filtrar"))
        #archive = archive.iloc[int(line)]
        #print(archive)
    #elif fil == 8:
        #column = str(input("Escribe el nombre de la columna que deseas filtrar"))
        #archive = archive[column]
    #elif fil == 9:
        #Pass
    #else:
        #Print("Eliga una opción de las disponibles")

def filter():
    print("Se mostrará el producto de acuerdo a su código")
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    introduceCode = int(input("Escribe el código de un producto"))
    archive = archive[archive["code"]==int(introduceCode)]
    print(archive)
    #acá se muestra las opciones de filtro y se selecciona la que irá en tipeFilter
    #print(filterOptions)
    #tipeFilter()

def modifi ():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print("Desea modificar algún producto")

def menu ():
    while True:
        print(options)
        posibility = int(input("Elija una opción: "))
        if posibility == 0:
            print("Quiere mirar el stock")
            wachStock()
            
        elif posibility == 1:
            print("Quiere agregar algún produto")
            addProduct()
            
        elif posibility == 2:
            print("Mostrar un producto especifico")
            filter()

        elif posibility == 3:
            print("Desea modificar algún producto")
            
        elif posibility == 4:
            print("Desea eliminar algún producto")
            
        elif posibility == 5:
            print("Extraer faltantes")
            
        elif posibility == 6:
            print("Extraer sobrantes")
            
        elif posibility == 7:
            print("Mostrar productos por vencer")
            
        elif posibility == 8:
            print("Cargar las ventas diarias")
            
        elif posibility == 9:
            print("Cargar las compras diarias")
            
        elif posibility == 10:
            print("Cargar las pérdidas")
        
        elif posibility == 11:
            print("El progama se cerrará inmediatamente")
            return False

        else:
            print("No seleccionó ninguna opción posible")
            

options= """"
===== Menú =====
0)_ Mirar el stock
1)_ Agregar algún producto
2)_ Filtrar producto
3)_ Modificar producto
4)_ Eliminar producto
5)_ Extraer faltante
6)_ Extraer sobrantes
7)_ Mostrar productos vencidos
8)_ Cargar ventas
9)_ Cargar pérdidas
10)_ Cargar compras
11)_ Salir del programa
"""
filterOptions="""
1)_ Para filtrar de acuerdo al código
2)_ Para filtrar de acuerdo a el nombre del producto
3)_ Para filtrar de acuerdo a la cantidad del producto
4)_ Para filtrar de acuerdo al costo del producto
5)_ Para filtrar de acuerdo a el beneficio del producto
6)_ Para filtrar de acuerdo al precio del producto
7)_ Para filtrar por filas
8)_ Para filtrar por columnas
9)_ Terminar el filtrado
"""
numberFilter="""
1)_ Una cantidad exacta
2)_ Una cantidad minima
2)_ Una cantidad máxima
"""
posibility = menu()