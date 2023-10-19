# Argumentos

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE='Integrated Development Envierement', PK='Primary Key')
listarTerminos(DBMS='DataBase Manage System')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'karla', 'Guillermo']
desplegarNombres(nombres)