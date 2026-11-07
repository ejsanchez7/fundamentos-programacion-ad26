# cadenas de texto
nombre1 = "Erik \"Profesor\""
nombre2 = 'Erik "Profesor"'

mensaje = "Esto es un mensaje\nde dos líneas"
mensaje_multilinea = """Esto es la primera línea
Esto es la segunda línea
Esto es la tercera línea"""

def reemplaza_caracter(texto, indice, valor):
    salida = ""
    #0, 1, 2, 3,..., 
    for posicion in range(len(texto)):
        if posicion == indice :
            salida += valor
        else:
            salida += texto[posicion]
    
    return salida

texto1 = "Hola mundo"
texto = "Hello world"
texto = reemplaza_caracter(texto, 5, "-")
texto1 = texto1.replace(" ", "-")

print(nombre1)
print(mensaje_multilinea)
print(texto[6])
print(texto1)
print(texto)