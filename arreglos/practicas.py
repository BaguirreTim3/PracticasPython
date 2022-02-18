import random


print('esto es un cadena de caracteres')


arreglo = [12, 25, 96, 87, 63, 98, 78, 63, 75]

for i in range(0, len(arreglo)):
    valor = arreglo[i]
    print(f'el valor {valor} esta pocision {i}' )

l = 20
lista = [random.randint(0, 100) for i in range(l)]
print(lista)

#ejemplo de como desestructurar en python 
productos = [
    {'nombre': 'jabon palmolive', 'precio': 12},
    {'nombre': 'leche en polvo', 'precio': 120},
    {'nombre': 'arroz pinillar', 'precio': 150}
]

productos.append({'nombre': 'jabon coco', 'precio': 1000})
productos.append({'nombre': 'jabon canalita', 'precio': 2000})

print(productos)

suma = 0

for i in range(0, len(productos)):
    elemento = productos[i]
    nombre, precio = elemento.values()
    print(precio)
    suma += precio
    
    
print(suma)  

print(5 + 6)