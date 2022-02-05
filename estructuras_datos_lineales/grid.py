from multiprocessing.dummy import Array
from arrays import Arrays


class Grid():
    def __init__(self, filas, columnas, valor=None):
        self.matrix = Arrays(filas)
        for fila in range(filas):
            self.matrix[fila] = valor
            
    