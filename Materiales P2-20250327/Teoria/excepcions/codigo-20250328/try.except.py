while True:
    try:
        dividendo = int(input('Introducir dividendo: '))
        divisor = int(input('Introducir divisor: '))
        cociente = dividendo / divisor
    except (ValueError, ZeroDivisionError):
        print('Error: valor incorrecto')
    except: # Resto excepciones
        print('Error desconocido')
    else:
        print('El resultado es ', cociente)
        break
    