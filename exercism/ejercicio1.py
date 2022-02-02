precios = {'manzana': 1000, 'huevo': 500}
cantidad = {'manzana': 2, 'huevo': 6}

valor = sum(precios[item] * cantidad[item] for item in cantidad)

for item in cantidad:
    print(precios[item])
    print(cantidad[item])
    
print(f'valor a pagar {valor}')