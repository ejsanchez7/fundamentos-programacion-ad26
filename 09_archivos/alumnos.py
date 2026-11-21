from funciones_archivos import abrir_archivo

RUTA_ARCHIVO = "./datos/alumnos.txt"

# Mostrar el promedio de cada alumno
def mostrar_promedios() :
    archivo = abrir_archivo(RUTA_ARCHIVO)
    
    for linea in archivo :
        # Borrar salto de línea del final y espacios en blanco del inicio
        linea = linea.strip("\n").strip()
        datos = linea.split(",")
        nombre = datos[0]
        suma = 0
        contador = 0

        for dato in datos :
            if dato.isnumeric() :
                suma += float(dato)
                contador += 1

        promedio = suma / contador
        print(f"{nombre}: {promedio}")
        
    archivo.close()

# Capturar las calificaciones de un alumno
def registrar_calificaciones() :
    nombre = input("Escribe el nombre del alumno: ")
    linea = nombre

    for i in range(3) :
        calificacion = input(f"Escribe la calificación {i + 1}: ")
        linea += f",{calificacion}"

    archivo = open(RUTA_ARCHIVO, "at")
    archivo.write(f"{linea}\n")
    archivo.close()

mostrar_promedios()
#registrar_calificaciones()