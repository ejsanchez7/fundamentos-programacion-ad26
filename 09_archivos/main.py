from funciones_archivos import abrir_archivo

# Tipos de archivos
# - texto
# - binarios

# Abrir archivos
# - Indicar el modo de apertura (lectura o escritura), default lectura
# - Indicar el tipo de archivo (texto o binario), default texto
# archivo = open("./prueba.txt") # lectura, texto
ruta_archivo = "./prueba.txt"
archivo = abrir_archivo(ruta_archivo, "r", "t") # devuelve un fileHandler

# leer
print(archivo.read()) # Devuelve todo el contenido del archivo en un string

# cerrar archivos
archivo.close()

# escribir
archivo_escritura = open("./prueba.txt", "wt") # Modo lectura, reemplaza todo el contenido
archivo_escritura.write("Cuarta línea\n")
archivo_escritura.close()

# append
archivo_append = open("./prueba.txt", "at") # modo append, agrega contenido al final
archivo_append.write("Nueva línea\n")
archivo_append.close()