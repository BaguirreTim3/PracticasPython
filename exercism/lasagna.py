"""en python un nombre de variable se puede por decirlo asi
    reutilizar como lo vemos en el siguiente ejemplo,
    mi_primera_variable se inicio con un valor de 10 pero
    luego se le pudo asignar otro valor con diferente tipo de dato
    por eso cuando la mando a imprimir por consola imprime el ultimo valor"""

from re import T
import string

    
mi_primera_variable = 10
mi_primera_variable = 'esto es una cadena'
print(mi_primera_variable)


"""en este ejemplo declaramos x con un valor inicial de 10, luego
    declaramos un funcion con nombre mostrar_x y dentro de esta funcion
    declaramos x con una valor tipo cadena de texto, luego mandamos a
    imprimir el valor de x que esta por fuera de la funcion y el valor de 
    x que esta dentro de la funcion y son completamente diferente""" 

x = 10

def mostrar_x():
    x = 'dentro de un funcion'
    return x
    
print(x)
new_x = mostrar_x()
print(new_x)    

#sintaxis para declarar funciones en python

def sumar(numero_uno, numero_dos):
    return numero_uno + numero_dos


resultado = sumar(5, 6)
print(resultado)    

def restar(numero_uno, numero_dos):
    resultado = numero_uno + numero_dos
    
print(restar)

def multiplicar(numero_uno, numero_dos=5):
    return numero_uno * numero_dos

resultado = multiplicar(5, 6)
print(resultado)  

print(string.ascii_lowercase)

mi_texto = 'Este es un texto en minusculas'

mi_texto_mayusculas = str.upper(mi_texto)
print(mi_texto_mayusculas)

#comentarios dentro de una funcion

def sumar(numero_uno, numero_dos):
    """ esta funcion recibira 
    dos numero y su objetivo es
    retornar el valor de la suma
    de esos dos numero"""
    
    return numero_uno + numero_dos


print(sumar.__doc__)

"""vas a escribir un codigo que te ayude a cocinar una lasagna"""

TIEMPO_DE_COCCION = 40

def tiempo_horneado_restante(tiempo_en_horno):
    return TIEMPO_DE_COCCION - tiempo_en_horno


def minutos_preparacion(numero_capas):
    return numero_capas * 2


def calcular_tiempo_total(cantidad_capas, minutos_horno):
    tiempo = tiempo_horneado_restante(minutos_horno)
    min_preparacion = minutos_preparacion(cantidad_capas)
    return min_preparacion + tiempo


salida = calcular_tiempo_total(10, 25) 
print(salida)   