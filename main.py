#primero hacer un menú
def menu ():
    while True:
        if posibility == 1:
            print("Quiere mirar el stock")
        elif posibility == 2:
            print("Quiere agregar algún produto")
        elif posibility == 3:
            print("Mostrar un producto especifico")
        elif posibility == 4:
            print("Desea modificar algún producto")
        elif posibility == 5:
            print("Desea eliminar algún producto")
        elif posibility == 6:
            print("Extraer faltantes")
        elif posibility == 7:
            print("Extraer sobrantes")
        elif posibility == 8:
            print("Mostrar productos por vencer")
        elif posibility == 9:
            print("Cargar las ventas diarias")
        elif posibility == 0:
            print("Cargar las compras diarias")
        elif posibility == 10:
            print("Cargar las pérdidas")
        else:
            print("No seleccionó ninguna opción posible")

options= """"
=== Menú ===
1)_ Mirar el stock
2)_ Agregar algún producto
3)_ Filtrar producto
4)_ Modificar producto
5)_ Eliminar producto
6)_ Extraer faltante
7)_ Extraer sobrantes
8)_ Mostrar productos vencidos
9)_ Cargar ventas
10)_ Cargar pérdidas
0)_ Cargar compras
"""

print(options)
posibility = int(input("Elija una opción\n"))
posibility = menu()