numero = int(input('Prporciona un valor entre 1 y 3: '))
numerotexto = ''

if numero == 1:
    numerotexto = 'Numero Uno'
elif numero == 2:
    numerotexto = 'Numero Dos'
elif numero == 3:
    numerotexto = 'Numero Tres'
else:
    numerotexto = 'Valor fuera de rango'

print(f'Numero Proporcionado: {numero} - {numerotexto}')