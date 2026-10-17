alumnos = {
    "A0348765": "Manuel Rodríguez",
    "A00888867": "Erik Sánchez",
    "A0435873": "María Ramírez"
}

print(alumnos["A00888867"]) # "Erik Sánchez"

alumnos_lista = [
    ["A0348765", "Manuel Rodríguez"], # alumnos_lista[0]
    ["A00888867", "Erik Sánchez"], # alumnos_lista[1]
    ["A0435873", "María Ramírez"] # alumnos_lista[2]
]

alumnos_lista[0][1] # "Manuel Rodríguez"
alumnos_lista[1][0] # "A00888867"


def calcula_histograma(lista) : #[1, 6, 4, 6, 8, 3, 1]
    histograma = {}
    # {1: 2, 6: 2, 4: 1, 8: 1, 3: 1}

    for elemento in lista :
        
        if elemento in histograma :
            histograma[elemento] += 1
        else :
            histograma[elemento] = 1

    return histograma

def imprime_asteriscos(cantidad) :

    #range(5) [0, 1, 2, 3, 4]
    #range(10, 15) [10, 11, 12, 13, 14]
    #range(10, 15, 2) [10, 12, 14]

    for i in range(cantidad) :
        print("*", end = "")

numeros = [1, 6, 4, 6, 8, 3, 1]
histograma = calcula_histograma(numeros)

for llave in histograma :
    cantidad = histograma[llave]
    print(f"{llave}: ", end = "")
    imprime_asteriscos(cantidad)
    print("")
