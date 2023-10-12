# Diccionarios

diccionario = {
    'IDE' : 'Integrated Development Enviroment',
    'OOP' : 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}

print(diccionario)
print(len(diccionario))
print(diccionario['IDE'])
print(diccionario.get('OOP'))
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

for termino, valor in diccionario.items():
    print(termino, valor)

print('IDE' in diccionario)

# - Agregar un elemento -
diccionario['PK'] = 'Primary Key'
print(diccionario)

# - Remover un Elemento -
diccionario.pop('DBMS')
print(diccionario)

# - Limpiar -
diccionario.clear()
print(diccionario)

# - Eliminar el diccionario -
del diccionario
print(diccionario) # NameError: name 'diccionario' is not defined