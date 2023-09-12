# Clases

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = 'Sin Alias') -> None:
        self.full_name = f'{name} {surname} {alias}' # Propiedad Publica
        self.__name = name # Propiedad Privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f'{self.full_name} Esta caminando')

my_person = Person('Christian', 'Arguello')
print(my_person.get_name())
print(my_person.full_name)
my_person.walk()

my_other_person = Person('Christian', 'Arguello', 'ChrisDev')
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = 'El loco de los perros'
print(my_other_person.full_name)

