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

def indentifica_primo(numero) :
    contador = 2

    if numero < 2 :
        return False
    
    while contador < numero :
        # Identifica divisor (no es primo)
        if numero % contador == 0 :
            return False
        # contador = contador + 1
        contador += 1
    return True

def encuentra_primos(inicio, fin) :
    contador = inicio

    while contador <= fin :
        if indentifica_primo(contador) :
            print(contador, end = ", ")
        contador += 1
    print("")
    
#generar_numeros(0, 5)
#print("-----------------")
#generar_numeros(10, 20, 2)
#encuentra_pares(25, 50)

# numero = int(input("Escribe un número: "))

# if indentifica_primo(numero) :
#     print(f"El número {numero} es primo")
# else :
#     print(f"El número {numero} no es primo")

desde = int(input("Escribe el valor de inicio: "))
hasta = int(input("Escribe el valor de fin: "))

encuentra_primos(desde, hasta)

# Programa que calcule el promedio de una lista de número
# Deberá pedir números al usuario de forma iterativa
# Si el usuario escribe la letra "n" el programa deberá parar 
# de pedir números
# Una vez que haya terminado de pedir números deberá devolver 
# el promedio