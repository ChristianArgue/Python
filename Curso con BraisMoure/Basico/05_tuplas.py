# Tuplas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (25, 1.69, 'Christian', 'Arguello')
my_other_tuple = (15, 30, 45)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Christian')) # Cuenta las veces que aparece lo mencioando

print(my_tuple.index('Arguello')) # Muestra en que posicion esta ubicado lo mencionado

# my_tuple[1] = 1.80 TypeError 'tuple' object does not support item assigment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)