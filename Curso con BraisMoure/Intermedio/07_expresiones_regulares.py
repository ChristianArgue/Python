# Expresiones Regulares

import re

my_string = 'Esta es la leccion numero 7: Leccion llamada Expresiones Regulares'
my_other_string = 'Esta no es la leccion numero 6: Manejo de Ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

print(re.match('Esta es la leccion', my_other_string))
print(re.match('Expresiones Regulares', my_string))

# Search

search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall

findall = re.findall('leccion', my_string, re.I)
print(findall)

# Split

print(re.split(':', my_string))

# Sub

print(re.sub('Expresiones', 'expresiones', my_string))
print(re.sub('leccion', 'LECCION', my_string))

# Patterns

pattern = r'[l|L]eccion'
print(re.findall(pattern, my_string))

pattern = r'[l|L]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z|A-Z|0-9]'
print(re.findall(pattern, my_string))

pattern = r'\d'
print(re.findall(pattern, my_string))

pattern = r'\D'
print(re.findall(pattern, my_string))

pattern = r'[l].*'
print(re.findall(pattern, my_string))

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.findall(pattern, email)

print(is_valid_email('christianarguello97@hotmail.com.ec'))  
is_valid_email('christianarguello97@hotmail.com.ec')  