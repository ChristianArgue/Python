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