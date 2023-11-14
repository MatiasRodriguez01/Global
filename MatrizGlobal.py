import random

class MatrizGlobal:

    def __init__(self):
        self.matrix = []
        self.size = 0
        self.diagonally = []
        self.average = 0

    def add_size(self):
        while True:
            self.size = int(input("Ingrese el tamaño de la matriz(El valor tiene que ser imapar): "))
            if (self.size % 2 != 0):
                return self.size

    def fill_matrix_automatically(self, size):
        for rows in range(size):
            list = []
            for columns in range(size):
                number = random.randint(1,99)
                list.append(number)
            self.matrix.append(list)
        return self.matrix
    
    def fill_matrix_manually(self, size):
        print("LLENE LA MATRIZ:")
        for rows in range(size):
            list = []
            for columns in range(size):
                number = int(input(f"Ingrese el valor de la fila {rows+1}: "))
                list.append(number)
            self.matrix.append(list)
        return self.matrix
    
    def fill_matrix(self, size):
        while True:
            print("Desea agrgar los numeros de la matriz:")
            print("1) manualmente.")
            print("2) automatica: ")
            option = int(input("opcion: "))
            print("----")
            matriz = []
            if option == 1:
                self.matriz = self.fill_matrix_manually(size)
                return self.matriz
            elif option == 2:
                self.matriz = self.fill_matrix_automatically(size)
                return self.matriz
            else:
                continue
    
    def show_matrix(self, matrix):
        for rows in self.matrix:
            print(rows)

    def fill_diagonally(self, size):
        if self.diagonally == []:
            for rows in range(size):
                for columns in range(size):
                    if (rows == columns):
                        number = self.matrix[rows][columns]
                        self.diagonally.append(number)
            return self.diagonally
    
    def average_diagonally(self):
        sum = 0
        counter = 0
        for elements in self.diagonally:
            sum += elements
            counter += 1
        self.average = round(sum/counter)
        return self.average
    
    def average_in_matrix(self, size):
        for rows in range(size):
            for columns in range(size):
                if self.average == self.matrix[rows][columns]:
                    self.average_True_false(True, rows, columns)
                    return True
        self.average_True_false(False, rows, columns)
        return False

    def average_True_false(self, value, row, column):
        if (value):
            print(f"EL promedio {self.average} esta en la matriz.")
            print(f"En la fila {row} y columa {column}.")
        else:
            print(f"EL promedio {self.average} no esta en la matriz.")


    
