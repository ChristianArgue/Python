# Tuplas

frutas = ('Naranja', 'Platano', 'Guayaba')
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[0:2])

for fruta in frutas:
    print(fruta, end= ', ')

# frutas[0] = 'Pera'
# print(frutas) 

fruta_lista = list(frutas)
fruta_lista[0] = 'Pera'
frutas = tuple(fruta_lista)
print(frutas)