def recorre_lista_while(lista) :
    indice = 0

    while indice < len(lista) :
        print(lista[indice], end = ", ")
        indice += 1

    print("")

def recorre_lista(lista) :
    for elemento in lista :
        print(elemento, end = ", ")
    print("")

def calcular_promedio(lista_numeros) :
    suma = 0
    
    for numero in lista_numeros :
        suma += numero

    return (suma / len(lista_numeros))

def pedir_numeros() :
    numeros = []
    
    entrada = input("Escribe un número o 'n' para terminar: ")
    
    while entrada != "n" :
        numero = float(entrada)
        numeros.append(numero)
        entrada = input("Escribe un número o 'n' para terminar: ")

    return numeros

# lista_numeros = pedir_numeros()
# print(lista_numeros)
# print(f"El promedio es {calcular_promedio(lista_numeros)}")

def encuentra_pares(lista_numeros) :
    pares = []

    for numero in lista_numeros :
        if numero % 2 == 0 :
            pares.append(numero)

    return pares

# lista_1 = [10, 21, 36, 48, 55]
# pares = encuentra_pares(lista_1)
# print(pares)

def clasifica_rangos(lista_numeros) :
    rangos = [0, 0, 0, 0] # [0] * 4

    for numero in lista_numeros :
        if numero >= 0 and numero <= 25 :
            rangos[0] += 1
        elif numero <= 50 :
            rangos[1] += 1
        elif numero <= 75 :
            rangos[2] += 1
        else :
            rangos[3] += 1

    return rangos

lista = [12, 3, 90, 56, 78]
rangos = clasifica_rangos(lista) # [2, 0, 1, 2]
print(rangos)

# recorre_lista_while(lista_1)
# recorre_lista(lista_1)
# print(calcular_promedio(lista_1))