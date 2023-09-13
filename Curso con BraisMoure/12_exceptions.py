# Exceptions

numberOne = 5
numberTwo = 1
numberTwo = "1"

# --- try except ---

try:
    print(numberOne + numberTwo)
    print('No se ha producido ningun error :)')
except:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error!')


# --- try except else ---

try:
    print(numberOne + numberTwo)
    print('No se ha producido ningun error :)')
except:
    print('Se ha producido un error!')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')


# --- try except else finally ---

try:
    print(numberOne + numberTwo)
    print('No se ha producido ningun error :)')
except:
    print('Se ha producido un error!')
else:
    # Se ejecuta si no se produce una excepcion
    print('La ejecucion continua correctamente')
finally:
    # Se ejecuta siempre
    print('La ejecucion continua')


# --- Excepciones por tipo ---

try:
    print(numberOne + numberTwo)
    print('No se ha producido ningun error :)')
except TypeError:
    # Se ejecuta si se produce una excepcion
    print('Se ha producido un error!')


# --- captura de la informacion de la excepcion ---

try:
    print(numberOne + numberTwo)
    print('No se ha producido ningun error :)')
except ValueError as e:
    print(e)
except Exception as e:
    print(e)