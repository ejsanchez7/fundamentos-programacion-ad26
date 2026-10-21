def multiplicar_columna(matriz, columna, valor) :
    for lista in matriz:
        lista[columna] = lista[columna] * valor

    return matriz

def imprime_matriz(matriz) :
    for lista in matriz:
        print(lista)


numeros = [
    [2, 5, 6, 4],
    [3, 4, 5, 1],
    [7, 8, 5, 6],
    [9, 7, 1, 5]
]

imprime_matriz(multiplicar_columna(numeros, 1, 4))
imprime_matriz(numeros)