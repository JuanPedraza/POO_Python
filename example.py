class Persona:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saluda(self, other_person):
        return f'Hola {other_person.name}, me llamo {self.name}'


juan = Persona('Juan', 30)
niyi = Persona('Niyi', 29)

juan.saluda(niyi)