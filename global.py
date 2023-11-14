import funciones_global as funciones
from MatrizGlobal import MatrizGlobal
import os

def clean_screen():
    tecla = input("Precione cualquier tecla para salir ")
    os.system('cls')
    

matriz = MatrizGlobal()
while True:
    print("MENU")
    print("1) Agregar el tamaño de la matriz.")
    print("2) Llenar la matriz.")
    print("3) Mostrar la matriz.")
    print("4) mostrar la diagonal principal de la matriz.")
    print("5) Muestre si el promedio de la diagonal, esta en la matriz.")
    print("6) salir")
    option = int(input("Opcion: "))
    if option == 1:
        os.system('cls')
        print("AGREGAR EL TAMAÑO DE LA MATRIZ:")
        matriz.add_size()
        clean_screen()
        continue
    elif option == 2:
        os.system('cls')
        if matriz.size == 0:
            print("La matriz no tiene tamaño asignado, primero agregelo!")
        else:
            matriz.fill_matrix(matriz.size)
        clean_screen()
        continue
    elif option == 3:
        os.system('cls')
        if matriz.matrix == []:
            print("La matriz esta vacia, primero llenela!")
        else:
            print("MATRIZ:")
            matriz.show_matrix(matriz.matrix)
        clean_screen()
        continue
    elif option == 4:
        os.system('cls')
        if matriz.matrix == []:
            print("La matriz esta vacia por lo que no puede hacer la diagonal, primero llenela!")
        else:
            matriz.fill_diagonally(matriz.size)
            print("DIAGONAL DE LA MATRIZ:")
            print(matriz.diagonally)
        clean_screen()
        continue
    elif option == 5:
        os.system('cls')
        if matriz.diagonally == []:
            print("La diagonal de la matriz esta vacia, no puede sacar el promedio")
        else:
            matriz.average_diagonally()
            print(f"El promedio de la diagonal es = ", matriz.average)
            average = 0; row = 0; column = 0
            matriz.average_in_matrix(matriz.size)
        clean_screen()
        continue
    elif option == 6:
        break
print("Ha salido del programa!!")

