"""
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion
y regresar como resultado la suma de todos los valores pasados como argumentos
"""

def sumaValores(*numeros):
    resultado = 0

    for n in numeros:
        resultado += n

    return resultado

print(sumaValores(4,3,3))