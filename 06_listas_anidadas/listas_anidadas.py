matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[2][1] #8
matriz[1][2] = 10

def recorre_matriz(matriz) :
    for lista in matriz :
        # lista = [1, 2, 3]
        for elemento in lista :
            print(elemento)