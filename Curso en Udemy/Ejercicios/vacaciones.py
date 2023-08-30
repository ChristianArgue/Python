# Verificar si puede asistir a los juegos solo si esta de vacaciones

vacaciones = False
diaDescanso = False

if (vacaciones or diaDescanso):
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')

if not(vacaciones or diaDescanso):
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')