# Crear una función que permita convertir temperaturas Kelvin, Celsius, Farenheit
# Celsius a Farenheit
# Farenheit a Celsius
# Celsius a Kelvin
# Kelvin a Celsius
# Farenheit a Kelvin

def celsius_to_farenheit(temperatura):
    try:
        resultado = (temperatura * 9/5) + 32
        return round(resultado)
    except:
        print("Valor no corresponde")

def farenheit_to_celsius(temperatura):
    try:
        resultado = (temperatura -32) * 5/9
        return round(resultado)
    except:
        print("Valor no corresponde")

def celsius_kelvin(temperatura):
    try:
        resultado = temperatura + 273.15
        return round(resultado)
    except:
        print("Valor no corresponde")

def kelvin_to_celsius(temperatura):
    try:
        resultado = temperatura - 273.15
        return round(resultado)
    except:
        print("Valor no corresponde")

def farenheit_to_kelvin(temperatura):
    try:
        resultado = (temperatura + 459.67) * 5/9
        return round(resultado)
    except:
        print("Valor no corresponde")

def kelvin_to_farenheit(temperatura):
    try:
        resultado = (temperatura * 9/5) - 459.67
        return round(resultado)
    except:
        print("Valor no corresponde")

def menu_conversiones():
    print("Seleccione la conversión a realizar")
    print("1. Celsius a Kelvin")
    print("2. Celsius a Farenheit")
    print("3. Kelvin a Celsius")
    print("4. Kelvin a Farenheit")
    print("5. Farenheit a Celsius")
    print("6. Farenheit a Kelvin")
    print("0. Detener programa")





continuar = "s"

while (continuar == "s" or continuar == "S" or continuar == "Si" or continuar == "si"):
    # Menú de selección
    menu_conversiones()
    
    # Selección
    try:
        seleccion = int(input("Su selección: "))
    except:
        pass

    # Conversiones
    try:
        if (seleccion == 1):
            temperatura = float(input("Ingrese la temperatura en celsius: "))
            print(celsius_kelvin(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 2):
            temperatura = float(input("Ingrese la temperatura en celsius: "))
            print(celsius_to_farenheit(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 3):
            temperatura = float(input("Ingrese la temperatura en kelvin: "))
            print(kelvin_to_celsius(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 4):
            temperatura = float(input("Ingrese la temperatura en kelvin: "))
            print(kelvin_to_farenheit(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 5):
            temperatura = float(input("Ingrese la temperatura en farenheit: "))
            print(farenheit_to_celsius(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 6):
            temperatura = float(input("Ingrese la temperatura en farenheit: "))
            print(farenheit_to_kelvin(temperatura))
            continuar = input("¿Desea realizar otra operación? [S/N]: ")
            
        elif (seleccion == 0):
            continuar = "n"
        else:
            print("El valor no es válido")
            continuar = input("¿Desea intentarlo de nuevo? [S/N]: ")
    except:
        print("Valor ingresado no corresponde")
        continuar = input("¿Desea intentarlo de nuevo? [S/N]: ")