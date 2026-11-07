#import math #importar la librería completa
#import math as mt #importar una librería y asignarle un alias
from math import pow, pi  # importa la función pow y la constante pi de la librería math

PI = pi

def calcular_area_rectangulo(largo, ancho) :
    return largo * ancho

def calcular_area_circulo(radio) :
    return PI * pow(radio, 2)
