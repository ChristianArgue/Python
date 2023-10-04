# Listas

nombres = ["Juan", "Karla", "Ricardo", "Maria"]

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[-1])
print(nombres[-2])
print(nombres[0:2])
print(nombres[:3])
print(nombres[1:])

nombres[3] = "Ivone"

print(nombres)

for nombre in nombres:
    print(nombre)
else:
    print('No existe mas nombres en la lista')

print(len(nombres))

nombres.append('Lorenzo')
print(nombres)

nombres.insert(1, 'Octavio')
print(nombres)

nombres.remove('Octavio')
print(nombres)

nombres.pop()
print(nombres)

del nombres[0]
print(nombres)

nombres.clear()
print(nombres)

del nombres
print(nombres)