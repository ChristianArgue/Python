# Funciones

def mi_funcion(nombre, apellido):
    print('Saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Christian', 'Arguello')
mi_funcion('Karla', 'Lara')

def sumar(a = 0, b = 0):
    return a + b

resultado = sumar(5, 3)
print(resultado)

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')