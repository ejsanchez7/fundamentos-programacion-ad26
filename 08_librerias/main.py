import geometria as geom

def imprime_menu() :
    print("1.- Área rectángulo")
    print("2.- Área círculo")
    return int(input("Opción --> "))

def calcular_area_rectangulo() :
    largo = float(input("Escribe el largo: "))
    ancho = float(input("Escribe el ancho: "))

    return geom.calcular_area_rectangulo(largo, ancho)

def calcular_area_circulo() :
    radio = float(input("Escribe el radio: "))

    return geom.calcular_area_circulo(radio)

opcion = imprime_menu()

match opcion :
    case 1 :
        print(f"El área del rectángulo es: {calcular_area_rectangulo()}")
    case 2 :
        print(f"El área del círculo es: {calcular_area_circulo()}")
    case _ :
        print("Opción inválida")