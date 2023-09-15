# Variables 
MyVariable = 'My String Variable'
print(MyVariable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenacion de variables en un print
print(MyVariable, my_int_to_str_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)
print('El numero es:', my_int_variable)

# Funciones del sistema
print(len(MyVariable))

# Variables en una sola linea. !No es recomendable usar esta sintaxis!
name, surname, alias, edad = 'Christian', 'Arguello', 'ChristianArgue', 25
print('Me llamo:', name, surname, ', mi alias es:', alias, 'y mi edad es:', edad)

# Inputs
'''
first_name = input('Cual es tu nombre?: ')
edad = input('Cual es tu edad?: ')
print(first_name)
print(edad)
'''

# Cambio de tipo
name = 34
age = 'Christian'
print(name)
print(age)

# Forzamos el tipo?
address: str = 'Mi Direccion'
address = 32
print(address)
print(type(address))