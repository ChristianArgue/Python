# Funciones

def my_function():
    print('Esto es una funcion')

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)

sum_two_values(25, 23)
sum_two_values('3', '4')

def sum_two_values_with_return(first_values, second_values):
    return first_values + second_values

result = sum_two_values_with_return(2, 2)
print(result)

def print_name(name, surname):
    print(f'{name} {surname}')

print_name('Moure', 'Brais')
print_name(surname= 'Moure', name= 'Brais')

def print_name_with_default(name, surname, alias = "Sin Alias"):
    print(f'{name} {surname} {alias}')

print_name_with_default("Brais", "Moure", "MoureDev")
print_name_with_default("Brais", "Moure")

def print_text(*text):
    print(text)

print_text('Hola', 'Python', 'ChrisDev')

def print_upper_texts(*texts):
    for text in texts:
        print(text)

print_upper_texts('Hola', 'Python', 'ChrisDev')