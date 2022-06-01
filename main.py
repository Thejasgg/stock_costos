#primero hacer un menú
from ast import Break
from fileinput import close
import os


def wachStock():
    archiveStock = "stock.txt"
    archive = open(archiveStock, "r")
    content = archive.read()
    print(content)
    archive.close()
    
#Arreglar la repetición ininita del menú y la función wachStock
def menu ():
    while True:
        print(options)
        posibility = int(input("Elija una opción: "))
        if posibility == 0:
            print("Quiere mirar el stock")
            wachStock()
            
        elif posibility == 1:
            print("Quiere agregar algún produto")
            #addProduct()
            
        elif posibility == 2:
            print("Mostrar un producto especifico")
            
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
=== Menú ===
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


posibility = menu()