from math import pi

# 1.- Definir PI = 3.1416
PI = 3.1416
# 2.- Pedir radio
radio = float(input("Escribe el radio: "))
# 3.- area = PI * radio ** 2
area = pi * radio ** 2
perimetro = pi * radio * 2
# 4.- mostrar area
print(f"El área es {area}")
print(f"El perímetro es {perimetro}")