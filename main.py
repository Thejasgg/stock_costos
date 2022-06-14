#primero hacer un menú
from ast import Break, Pass, main
from ctypes.wintypes import BOOLEAN
from fileinput import close
import os
from this import d
from numpy import datetime_data
import pandas as pd
from datetime import date, time, datetime


def wachStock():
    #archiveStock = "Stock.txt"
    #archive = open(archiveStock, "r")
    #content = archive.read()
    #print(content)
    #archive.close()
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print(archive)

def save():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print(saveOptios)
    save = int(input("Elija una opción: "))
    if save == 1:
        print("Los cambios se guardarán inmediatamente")
        archive.to_excel("base de datos de stock.xlsx")
    elif save == 2:
        print("No se guardarán los cambios")

def addProduct():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print("Se añadirá un producto")
    #archiveStock = "Stock.txt"
    #archive = open(archiveStock, "w")
    newProduct = {"code":"","product":"","stock":"","cost":"","benefit":"","income":"","date":""}
    newProduct["code"] = input("Escribe el código del nuevo producto: ")
    newProduct["product"] = str(input("Escribe el nombre del producto: "))
    newProduct["inventary"] = int(input("Escribe la cantidad del producto: "))
    newProduct["cost"] = float(input("Escribe cual fue el costo del producto: "))
    newProduct["benefit"] = float(input("Escribe cual es el margen de ganancias del producto: "))
    newProduct["price"] = float(input("Escribe cual es el precio del producto: "))
    caducatedDate = str(input("Escribe la fecha de caducidad: "))
    dateProduct = datetime.strptime(caducatedDate, "%d/%m/%y")
    newProduct["date"] = dateProduct
    archive = archive.append(newProduct, ignore_index=True)
    print(archive)
    save()

def cantFilter():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    while True:
        print(numberFilter)
        filterCant = int(input("Seleccione como desea filtrar la cantidad: "))
        if filterCant == 1:
            cantProduct = int(input("Escribe la cantidad del producto: "))
            archive = archive[archive["inventary"]==int(cantProduct)]
            print(archive)
        elif filterCant == 2:
            cantProduct = int(input("Escribe la cantidad minima del producto: "))
            archive = archive[archive["inventary"]>=int(cantProduct)]
            print(archive)
        elif filterCant == 3:
            cantProduct = int(input("Escribe la cantidad máxima del producto: "))
            archive = archive[archive["inventary"]<=int(cantProduct)]
            print(archive)
        elif filterCant == 4:
            return False
        else:
            print("No eligio ninguna de las opciones posibles")

def filter():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    while True:
        print(filterOptions)
        fil = int(input("Escriba el identificador del filtro que desea aplicar: "))
        if fil == 1:
            introduceCode = int(input("Escribe el código de un producto: "))
            archive = archive[archive["code"]==int(introduceCode)]
            print(archive)
        elif fil == 2:
            nameProduct = str(input("Escribe el nombre de un producto: "))
            archive = archive[archive["product"]==str(nameProduct)]
            print(archive)
        elif fil == 3:
            cantFilter()
        elif fil == 4:
            costProduct = float(input("Escribe el costo de un producto: "))
            archive = archive[archive["cost"]==float(costProduct)]
            print(archive)
        elif fil == 5:
            benefitProduct = float(input("Escribe el beneficio del producto: "))
            archive = archive[archive["benefit"]==float(benefitProduct)]
            print(archive)
        elif fil == 6:
            priceProduct = float(input("Escribe el beneficio del producto: "))
            archive = archive[archive["price"]==float(priceProduct)]
            print(archive)
        elif fil == 7:
            line = int(input("Escriba el número de la fila que desea filtrar: "))
            archive = archive.iloc[int(line)]
            print(archive)
        elif fil == 8:
            column = str(input("Escribe el nombre de la columna que deseas filtrar: "))
            archive = archive[column]
            print(archive)
        elif fil == 9:
            caducatedDate = str(input("Escribe la fecha de caducidad: "))
            dateProduct = datetime.strptime(caducatedDate, "%d/%m/%y")
            print(dateProduct)
            archive = archive[archive["date"]==(dateProduct)]
            print(archive)
        elif fil == 10:
            return False
        else:
            print("Eliga una opción de las disponibles")

#def filter():
    #print("Se mostrará el producto de acuerdo a su código")
    #archiveStock = "Base de datos de stock.xlsx"
    #archive = pd.read_excel(archiveStock)
    #introduceCode = int(input("Escribe el código de un producto: "))
    #archive = archive[archive["code"]==int(introduceCode)]
    #print(archive)
    #acá se muestra las opciones de filtro y se selecciona la que irá en tipeFilter
    #print(filterOptions)
    #tipeFilter()

def modifi ():
    #archiveStock = "Base de datos de stock.xlsx"
    #archive = pd.read_excel(archiveStock)
    print("Desea modificar algún producto")
    while True:
        print(optionsModifi)
        mod = int(input("Elija una de las opciones de modificar: "))
        if mod == 1:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escribe el código de un producto: "))
            newCode = int(input("Escribe el nuevo código: "))
            archive.loc[archive["code"]==introduceCode, "code"] = int(newCode)
            print(archive)
            save()
            
        elif mod == 2:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            nameProduct = str(input("Escribe el nombre de un producto: "))
            print(nameProduct)
            newNameProduct = str(input("Escribe el nuevo nombre del producto: "))
            print(newNameProduct)
            archive.loc[archive["product"]==nameProduct, "product"] = str(newNameProduct)
            print(archive)
            save()

        elif mod == 3:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escirbe el código del producto: "))
            cantProduct = int(input("Escribe la cantidad actual del producto: "))
            NewCantProduct = int(input("Escribe la nueva cantidad: "))
            archive.loc[(archive["inventary"]==cantProduct) & (archive["code"]==int(introduceCode)), "inventary"] = int(NewCantProduct)
            print(archive)
            save()

        elif mod == 4:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escirbe el código del producto: "))
            costProduct = float(input("Escribe el costo de un producto: "))
            newCostProduct = float(input("Escribe el nuevo costo del producto: "))
            archive.loc[(archive["cost"]==float(costProduct)) & (archive["code"]==int(introduceCode)), "cost"] = float(newCostProduct)
            print(archive)
            save()
        
        elif mod == 5:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escirbe el código del producto: "))
            benefitProduct = float(input("Escribe el beneficio del producto: "))
            newBenefitProduct = float(input("Escribe el nuevo benedifio del producto: "))
            archive.loc[(archive["benefit"]==float(benefitProduct)) & (archive["code"]==int(introduceCode)), "benefit"] = float(newBenefitProduct)
            print(archive)
            save()
        
        elif mod == 6:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escirbe el código del producto: "))
            priceProduct = float(input("Escribe el beneficio del producto: "))
            newPriceProduct = float(input("Escribe el nuevo beneficio: "))
            archive.loc[(archive["price"]==float(priceProduct)) & (archive["code"]==int(introduceCode)), "price"] = float(newPriceProduct)
            print(archive)
            save()

        elif mod == 7:
            archiveStock = "Base de datos de stock.xlsx"
            archive = pd.read_excel(archiveStock)
            introduceCode = int(input("Escirbe el código del producto: "))
            caducatedDate = str(input("Escribe la fecha de caducidad: "))
            dateProduct = datetime.strptime(caducatedDate, "%d/%m/%y")
            newCaducatedDate = str(input("Escribe la nueva fecha de caducidad: "))
            newDateProduct = datetime.strptime(newCaducatedDate, "%d/%m/%y")
            archive.loc[(archive["date"]==dateProduct) & (archive["code"]==int(introduceCode)), "date"] = newDateProduct
            print(archive)
            save()
        
        elif mod == 8:
            return False
        
        else:
            print("Eliga una opción de las disponibles")

def deleteProduct():
    print("Desea eliminar un producto")
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    introduceCode = int(input("Escribe el código del producto a eliminar: "))
    forDelete = archive[archive["code"]==int(introduceCode)].index
    print(forDelete)
    archive = archive.drop(forDelete)
    print(archive)
    save()

#def calculatorMissing(inventary):
    #inventary = inventary + 3
    #return inventary

def missing():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print("Va a extraer los faltantes")
    introduceCode = int(input("Escribe el código del producto: "))
    cantMissing = int(input("Escribe la cantidad de faltante: "))
    archive.loc[archive["code"]==introduceCode, "inventary"]-= cantMissing
    #inventary = int(input("Escribe la cantidad que deseas cambiar"))
    #def calculatorMissing(inventary):
        #archive.loc[archive["code"]==introduceCode, "inventary"] = inventary - cantMissing
        #print(archive)
        #return inventary
    #inventary = archive["inventary"]
    #archive["inventary"] = archive["inventary"].apply(calculatorMissing)
    print(archive)
    save()

def excess():
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    print("Desea actualizar el stock con los excedentes de productos")
    introduceCode = int(input("Escribe el código del producto: "))
    cantExcess = int(input("Escribe la cantidad de sobrante: "))
    archive.loc[archive["code"]==introduceCode, "inventary"]+= cantExcess
    print(archive)
    save()


def expire():
    print("Productos por expirar en base a una fecha determinada")
    archiveStock = "Base de datos de stock.xlsx"
    archive = pd.read_excel(archiveStock)
    caducatedDate = str(input("Escribe la fecha que considere para tener en cuenta la caducidad: "))
    dateProduct = datetime.strptime(caducatedDate, "%d/%m/%y")
    archive = archive.loc[(archive["date"]<=dateProduct)]
    print(archive)

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
            modifi()
            
        elif posibility == 4:
            print("Desea eliminar algún producto")
            deleteProduct()

        elif posibility == 5:
            print("Extraer faltantes")
            missing()

        elif posibility == 6:
            print("Extraer sobrantes")
            excess()

        elif posibility == 7:
            print("Mostrar productos por vencer")
            expire()

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
9)_ Para filtrar por fechas de caducidad
10)_ Para dejar de filtrar
"""
numberFilter="""
1)_ Una cantidad exacta
2)_ Una cantidad minima
3)_ Una cantidad máxima
4)_ Dejar de filtrar por cantidad
"""
optionsModifi="""
1)_ Modificar el código del producto
2)_ Modificar el nombre del producto
3)_ Modificar la cantidad en stock del producto
4)_ Modificar el costo del producto
5)_ Modificar el beneficio sobre el producto
6)_ Modificar el precio del beneficio
7)_ Modificar la fecha de caducidad de un producto
8)_ Dejar de modificar
"""
saveOptios="""
1)_ Guardar
2)_ Cerrar sin guardar
"""
posibility = menu()