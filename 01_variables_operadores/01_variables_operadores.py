# Variables (sintaxis)

# 01_variable = 10 # Nombre no válido
_variable = 10 # Válido
variable_01 = 10 # válido

# mi_variable # Error, una variable siempre debe tener un valor asignado

# Tipos de datos nativos / escalares
numero_entero = 123
numero_decimal = 123.45
booleano = True # False
variable_string = "Hola mundo"

# Compuestos o complejos
lista = [1, 2, 3, 4]

#Operador de asignación
mi_variable = 20

# Operadores matemáticos (devuelven números)
suma = 5 + 9.5
resta = 24 - 123
multiplicacion = 34 * 56
division = 45 / 9
division_entera = 45 // 7 #6
modulo_residuo = 45 % 7 #3
potencia = 2 ** 8 # 256
raiz = 2 ** (1 / 2)

# Jerarquía
# 1.- ()
# 2.- **
# 3.- * / % //
# 4.- + -

# Operadores relacionales (booleanos)
# < > == === <= >= != !== !

celsius = 689
fahrenheit = celsius * (9/5) + 32 # 1272.2

#Imprimir valores en la terminal
print(fahrenheit)
print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")

# Pedir información al usuario
calificacion_1 = float(input("Escribe la primer calificación: "))
calificacion_2 = float(input("Escribe la segunda calificación: "))
calificacion_3 = float(input("Escribe la tercer calificación: "))

promedio = (calificacion_1 + calificacion_2 + calificacion_3) / 3

print(f"El promedio es: {promedio}")