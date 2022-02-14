print("hola mi nombre", " es bremys", " y tengo 35", sep="...")

nombre = 'bremys'
edad = 37
saludo = 'hola,'
pregunta = '¿como estas hoy?'
#nombre = input("¿Cual es tu nombre: ")


print("Soy", nombre, end=" ")
print("y tengo", edad, "años")
print("cumplidos")
print(saludo, nombre, pregunta)


#monedas = int(input("¿Cuantas monedas tienes? "))
#siguiente = monedas + 1
#print("yo tengo mas. tengo", siguiente)

#t = float(input("¿en cuantos seg corres 100m? "))
#dif = t - 9.58
#print("Eres ", dif, "segundos mas lento que Bolt")

#dato = bool(input("Ingresa tu nombre: "))
#print("Nombre ingresado ", dato)
#print("¿cuantos billetes de 1000 tienes")
#a = input()
#print("tienes" + str(int(a) * 100000) )





def velocidad(distancia, tiempo):
    resultado = ""
    segundo = 3600
    metros = 1000
    kilometro_por_hora = (distancia / tiempo)
    metros_por_segundo = (kilometro_por_hora * metros) / segundo
    resultado = "La velocidad es " + str(round(kilometro_por_hora, 2)) + "km/h o " 
    str(round(metros_por_segundo, 2)) + "m/s"
    
    return resultado
    


salida = velocidad(1, 10800/3600)
print(salida) 
print(type(salida))
print((True or True) and (True))