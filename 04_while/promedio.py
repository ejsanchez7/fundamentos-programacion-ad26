# programa que pida números al usuario hasta que escriba "n"
# Después devuelve el promedio
def calcula_promedio() :
    suma = 0
    contador = 0
    
    entrada = input("Escribe un número o 'n' para terminar: ")
    
    while entrada != "n" :
        numero = float(entrada)
        suma += numero
        contador += 1
        entrada = input("Escribe un número o 'n' para terminar: ")

    return (suma / contador)

print(f"El promedio es: {calcula_promedio()}")