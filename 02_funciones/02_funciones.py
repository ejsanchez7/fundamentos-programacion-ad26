# *************************
# Definición de funciones
# *************************
promedio = 0
suma = 0

# Funciones que no reciben parámetros (procedimientos)
def mostrar_menu() :
    print("1.- Sumar tres números.")
    print("2.- Calcular promedio.")
    opcion = int(input("Selecciona una opción:"))

    return opcion

def calcular_suma(num_1, num_2, num_3) :
    suma = num_1 + num_2 + num_3
    return suma

# Funciones que reciben parámetros
def calcular_promedio(num1, num2, num3) :
    promedio = calcular_suma(num1, num2, num3) / 3
    return promedio

# *************************
# Uso de funciones
# *************************
opcion = mostrar_menu() #1, 2
print(f"La opción seleccionada es: {opcion}")

n1 = 1
n2 = 2
n3 = 3

calcular_suma(n1, n2, n3)
print(calcular_promedio(1, 2, 3))
prom = calcular_promedio(4, 5, 6)
print(prom)
