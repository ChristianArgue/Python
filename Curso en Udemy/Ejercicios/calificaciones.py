#-------------------------------------------------------------------------------------
#| Instrucciones del ejercicio:                                                      |
#|                                                                                   |  
#| El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:      |
#| El usuario proporcionara un valor entre 0 y 10.                                   |
#|                                                                                   |
#| Si esta entre 9 y 10 - imprimir una A                                             | 
#| Si esta entre 8 y menor a 9 - imprimir una B                                      |
#| Si esta entre 7 y menor a 8 - imprimir una C                                      |
#| Si esta entre 6 y menor a 7 - imprimir una D                                      |  
#| Si esta entre 0 y menor a 6 - imprimir una F                                      |
#|                                                                                   |
#| Cualquier otro valor debe imprimir - Valor incorrecto                             |
#|                                                                                   |
#| Por ejemplo:                                                                      |
#|                                                                                   |
#| Proporciona un valor entre 0 y 10:                                                |   
#| 'A'                                                                               |
#|                                                                                   |
#-------------------------------------------------------------------------------------

nota = float(input('Porporciona una calificacion entre 0 y 10: '))
ponderacion = None

if 9 < nota <= 10:
    ponderacion = 'A'
elif 8 < nota <= 9:
    ponderacion = 'B'
elif 7 < nota <= 8:
    ponderacion = 'C'
elif 6 < nota <= 7:
    ponderacion = 'D'
elif 0 < nota <=6:
    ponderacion = 'F'    
else:
    print('El valor no esta dentro del rango de la tabla de calificaciones')

print(f'Tu nota de {nota} tiene una ponderacion de {ponderacion}')