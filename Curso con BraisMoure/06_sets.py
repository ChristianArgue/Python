# Sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Christian', 'Arguello', 25}
print(type(my_other_set))

print(len(my_other_set))

# print(my_other_set[0])

my_other_set.add('ChrisDev')
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('ChrisDev')
print(my_other_set) # Un set no admite repetidos

print('Arguello' in my_other_set)
print('Mera' in my_other_set)

my_other_set.remove('Arguello')
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
# print(my_other_set) 

my_set = {'Brais', 'Moure', 34}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Pyhton', 'Swift'}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.difference(my_set))