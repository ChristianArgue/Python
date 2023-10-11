# Dada la siguiente tupla, crear una lista que solo incluya
# los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []

for t in tupla:
    if t < 5:
        lista.append(t)

print(lista)