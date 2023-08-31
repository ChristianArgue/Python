# Listas
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [25, 1.69, 'Christian', 'Arguello']
print(my_other_list)
print(type(my_other_list))
print(my_other_list[0])
print(len(my_other_list) - 1 )

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append('ChrisDev') # Agrega un elemento al final de la lista
print(my_other_list)

my_other_list.insert(1, 'Azul') # Agrega un elemento a la lista en la posicion que deseamos
print(my_other_list)

my_other_list.remove('Azul') # Elimina el item selecionado en la lista
print(my_other_list)

my_list.remove(30) # Elimina el item selecionado
print(my_list)

my_list.pop() # Elimina el ultimo item de la lista
print(my_list)

my_list.pop(2) # Elimina el item en la posicion selecionada
print(my_list)

del my_list[2] # Elimina por completo el item en la posicion selecionada
print(my_list)

my_new_list = my_list.copy() # Hace una copia de la lista y la guarda en otra variable

my_list.clear() # Elimina toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Hace el inverso de la lista
print(my_new_list)

my_new_list.sort() # Ordena la lista
print(my_new_list)