# Ingresar los datos necesarios para completar la informacion de libro
# Nombre, ID, Precio, Envio Gratuito

print("")

print('Proporcione los siguientes datos del libro')

print("")

nombre = input('Nombre del libro: ')
identificacion = int(input('ID del libro: '))
precio = float(input('Precio del libro: '))
envio = input('Indique si el envio es gratuito (True/False): ')

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    print('Valor incorrecto, debe escribir True/False')

print("")

print(f'''
Nombre: {nombre},
ID: {identificacion},
Precio: {precio},
Envio Gratuito?: {envio}
''')
# print(f'Nombre: {nombre}')
# print(f'ID: {identificacion}')
# print(f'Precio: {precio}')
# print(f'Envio Gratuito?: {envio}')