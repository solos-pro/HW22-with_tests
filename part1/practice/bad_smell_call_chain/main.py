# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person1:
    def __init__(self):
        self.planet = Planet()

    def get_person_room(self):
        return self.planet.get_contry().get_city().get_street().get_room().get_name()

    def get_city_population(self):
        return self.planet.get_contry().get_city().population()


class Person:
    def __init__(self, planet='Eath', country='country', city='city', street='street', room='room', name='name', population=2):
        self.planet = planet
        self.country = country
        self.city = city
        self.street = street
        self.room = room
        self.name = name
        self.population = population

    def get_planet(self):
        return self.planet

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_street(self):
        return self.street

    def get_person_room(self):
        return self.room

    def get_name(self):
        return self.name

    def get_city_population(self):
        return self.population


person = Person("Eath", "Russia", "Voronezh", "prospect", 42, "Piter", 100500)
print(person.get_person_room())
person.get_person_room()
print(person.get_city_population())
# после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.