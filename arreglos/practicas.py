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
evon = [
    {'nombre': 'jabon palmolive', 'precio': 12},
    {'nombre': 'leche en polvo', 'precio': 120},
    {'nombre': 'arroz pinillar', 'precio': 150}
]

evon.append({'nombre': 'jabon coco', 'precio': 1000})

print(evon)

suma = 0

for i in range(0, len(evon)):
    elemento = evon[i]
    nombre, precio = elemento.values()
    print(precio)
    suma += precio
    
    
print(suma)    
      