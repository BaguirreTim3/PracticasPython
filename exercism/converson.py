#numbers python
import math

print(3 + 3.6)
print(3 * 3.6)
print(3 - 2.5)

#parte entera
print(6 // 2)
print(7 // 4)

#modulo
print(7 % 4)
print(2 % 4)
print(12.75 % 3)
#convertir de float a entero
#convertir de entero a float

print(int(12.75 / 3))
print(float(3 + 5))

millon = 1_000_000
print(millon)

def exchange_money(budget, exchange_rate):
    return budget * exchange_rate


def get_change(budget, echanging_value):
    return budget - echanging_value


def get_value_of_bills(denomination, number_of_bills):
    bono, factura = math.modf(denomination * number_of_bills)
    return [bono, factura]
    

def get_number_of_bill(budget, denomination):
    return budget // denomination    
    
salida = exchange_money(127.5, 1.2)
result = get_change(127.5, 120)
resultado = get_value_of_bills(5, 128.5)
res = get_number_of_bill(127.5, 5)

print(salida)
print(result)
print(resultado)
print(res)