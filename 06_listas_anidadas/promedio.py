def promedia_matriz(matriz) :
    suma = 0
    contador = 0

    for lista in matriz :
        for numero in lista :
            suma += numero
            contador += 1

    matriz[1][1] = 25
    return (suma / contador)


numeros = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

print(f"El promedio es: {promedia_matriz(numeros)}")