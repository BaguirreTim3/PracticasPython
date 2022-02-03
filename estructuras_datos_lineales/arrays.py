from operator import itemgetter
import random
from functools import reduce

class Arrays:
    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
      
            
    def __len__(self):
        return len(self.items)        
    
        
    def __str__(self):
        return str(self.items)


    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, nuevo_elemento):
        self.items[index] = nuevo_elemento
    
    def __llenar_aleatoreo__(self):
       return [self.__setitem__(i, random.randint(0, 100)) for i in range(
               self.capacity)]
    
    
    def __sum__(self):
        return reduce(lambda x, y: x + y, self.items)
        
          
        
            
    
    if __name__ == '__main__':
        
        from arrays import Arrays
        
        arreglo = Arrays(5)
        print(len(arreglo))
        print(arreglo)
        
        for i in range(len(arreglo)):
            arreglo[i] = i + 1
            
        
        print(arreglo)
        arreglo.__setitem__(2, 21)
        print(arreglo)
        arreglo.__llenar_aleatoreo__()
        sumatoria = arreglo.__sum__()
        print(arreglo)
        print(sumatoria)
            