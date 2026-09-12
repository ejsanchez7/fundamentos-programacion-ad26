# Función que reciba 2 números y devuelva el mayor
def obtiene_mayor(num1, num2) :
    # SI num1 > num2
    if num1 > num2 :
        # Devolver num1
        return num1
    # SINO
    else :
        return num2

# numero1 = int(input("Escribe un numero: ")) #5
# numero2 = int(input("Escribe otro numero: ")) #10

# mayor = obtiene_mayor(numero1, numero2)
# print(f"El mayor entre {numero1} y {numero2} es: {mayor}")

def calcular_corriente(voltaje, resistencia) :

    if resistencia > 0 :
        corriente = voltaje / resistencia
        # return (voltaje / resistencia)
        # Este return rompe la función y evita que se ejecute lo que sigue
        return corriente

    print("La resistencia debe ser mayor a 0")
    # El return sirve para devolver un valor y terminar la función
    # Este return solo se ejecutaría si no se entra al if
    return False

# volt = float(input("Escribe el voltaje: "))
# res = float(input("Escribe la resistencia: "))
# corriente = calcular_corriente(volt, res)

# Valores considerados como verdaderos en python
#   cualquier número mayor a 0
#   True
#   cualquier texto con contenido
#   None
#   Listas vacías
# if corriente :
#     print(f"La corriente es: {corriente}")

def obtiene_tipo_triangulo(a, b, c) :# 2, 5, 4
    # La suma de dos lados es mayor al otro
    if (a + b > c) and (a + c > b) and (b + c > a) :
        # Equilátero
        if (a == b) and (b == c) :
            print("Es equilátero")
        # Isóseles
        elif (a == b) or (a == c) or (c == b) :
            print("Es isóseles")
        else :
            print("Es escaleno")

        return True
    else:
        print("No es un triángulo")
        return False

obtiene_tipo_triangulo(2, 5, 4)