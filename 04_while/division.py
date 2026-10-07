def dividir(numerador, denominador) : #25, 10
    residuo = numerador
    contador = 0

    while residuo >= denominador :
        contador += 1
        residuo -= denominador

    print(f"La división de {numerador}/{denominador} es {contador}")
    print(f"El residuo de {numerador}/{denominador} es {residuo}")

dividir(25, 5)
dividir(100, 9)