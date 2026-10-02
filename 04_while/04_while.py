# Si al invocar la función solo se pasan dos parámetros salto sería 1
def generar_numeros(desde, hasta, salto = 1) :
    contador = desde
    #depende de una condición
    while contador <= hasta :
        if contador < hasta :
            print(contador, end = ", ")
        else :
            print(contador)
        # Las variables de la condición deben cambiar dentro del while
        contador = contador + salto
        # Rompe cualquier ciclo (pero no la función)
        #break

# Imprima los números pares entre a y b
def encuentra_pares(inicio, fin) : #25, 50
    contador = inicio
    incremento = 1

    while contador <= fin :
        if (contador % 2) == 0 :
            print(contador, end = ", ")
            incremento = 2
        contador = contador + incremento
    print("")

#generar_numeros(0, 5)
#print("-----------------")
#generar_numeros(10, 20, 2)
encuentra_pares(25, 50)