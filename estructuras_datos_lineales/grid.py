from multiprocessing.dummy import Array
from arrays import Arrays


class Grid():
    def __init__(self, filas, columnas, valor=None):
        self.matrix = Arrays(filas)
        for fila in range(filas):
            self.matrix[fila] = Arrays(columnas, valor)
    
    
    def get_heigth(self):
        return len(self.matrix)
    
    
    def get_weigth(self):
        return len(self.matrix[0])


    def __getitem__(self, index):
        return self.matrix[index]
    
    
    def __str__(self):
        result = ""
        
        for row in range(self.get_heigth()):
            for col in range(self.get_weigth()):
                result += str(self.matrix[row][col]) + " "
            result += "\n"
        return str(result)        



if __name__ == '__main__':
    
    from grid import Grid
    
    mat = Grid(4, 6)
    
    for row in range(mat.get_heigth()):
        for col in range(mat.get_weigth()):
            mat[row][col] = row * col 
            
            
    print(mat)
    
    print(mat.__getitem__(2)[2])
    print(mat.__str__())        
            
            
    