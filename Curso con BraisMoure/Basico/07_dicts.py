# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {'Nombre':'Christian', 'Apellido':'Arguello', 'Edad':25, 1:'Python'}
my_dict = {
    'Nombre':'Christian', 
    'Apellido':'Arguello', 
    'Edad':25, 
    'Lenguajes':{'Python', 'Swift', 'Kotlin'},
    1:1.69
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict['Nombre'])

my_recovery_dict = my_dict.copy()

my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre'])
print(my_dict[1])

my_dict['Calle'] = 'Calle Arguello'
print(my_dict)

my_dict.pop('Nombre')
print(my_dict)

del my_dict['Calle']
print(my_dict)

my_dict['Nombre'] = 'Christian'
print(my_dict)

my_dict.pop('Nombre')
print(my_dict)

print('Arguello' in my_dict)
print('Apellido' in my_dict)

print(my_recovery_dict.items())
print(my_recovery_dict.keys())
print(my_recovery_dict.values())
# print(my_recovery_dict.fromkeys())

my_new_dict = dict.fromkeys(my_recovery_dict)
print(my_new_dict)

# my_new_dict = dict.fromkeys(my_recovery_dict, my_recovery_dict.values())
# print(my_new_dict)

# my_new_dict['Nombre'] = 'Christian'
# print(my_new_dict)