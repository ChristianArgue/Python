# Strings
my_string = 'Mi String'
my_outher_string = 'Mi otro String'

print(len(my_string))
print(len(my_outher_string))

print(my_string + ' ' + my_outher_string)

my_new_line_string = 'Este es un string \ncon salto de linea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulacion'
print(my_tab_string)

my_scape_string = '\tEste es un string \n escapdo'
print(my_scape_string)

# Formateo
name, surname, age = 'Christian', 'Arguello', 25
print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age))
print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age))
print(f'Mi nombre es {name} {surname} y mi edad es {age}')