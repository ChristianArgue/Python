"""
Crear un funcion para multiplicar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la multiplicacion de todos los valores pasados como argumentos.
"""

def multiplicacion(*valores):
    numero = 1
    for i in valores:
        numero *= i
    
    return numero

resultado = multiplicacion(7, 5, 5)
print(resultado)