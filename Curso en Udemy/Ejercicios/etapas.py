# Etapas de la vida

# 0-10 - La infancia es increible
# 10-20 - Muchos cambios y mucho estudio
# 20-30 - Amor y comienza el trabajo
# Cualquier otro valor - Etapa de vida no reconocida

edad = int(input('Proporciona tu edad: '))

if 0 <= edad < 10:
    print(f'Tu edad de {edad} tiene La infancia es increible')
elif 10 <= edad < 20:
    print(f'Tu edad de {edad} va haber Muchos cambios y mucho estudio')
elif 20 <= edad < 30:
    print(f'Tu edad de {edad} habra Amor y comienza el trabajo')
else:
    print(f'La edad de {edad}, Etapa de vida no reconocida')
