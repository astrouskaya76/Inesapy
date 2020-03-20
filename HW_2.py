
# 1
class car:
    def __init__(self, wheel, model, speed):
        self.wheel = wheel
        self.model = model
        self.speed = speed

    def myfunc(self):
        print(self.wheel, self.model, self.speed)


ford = car(4, "Ford", 60)
jeep = car(4, "Jeep", 65)
ford.myfunc()
jeep.myfunc()


# 2
class car:
    wheel = 4
    model = "A"
    speed = 500

    def __init__(self, wheel, model, speed):
        self.wheel = wheel
        self.model = model
        self.speed = speed

    def myfunc(self):
        print("Car:", + self.wheel, self.model, self.speed)


ford = car(4, "Ford", 60)
jeep = car(4, "Jeep", 65)
ford.myfunc()
jeep.myfunc()


# 2
class food:
    pass


fruit1 = food()
fruit2 = food()
fruit2.newValue = 5


# 3
class food:
    name = "A"
    weight = 15

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def myfunc(self):
        print(self.name, self.weight)


a = food("apple", 12)
a.myfunc()


# 4 - #5


class Car:  # Создание класса
    wheels = 4  # Несколько полей
    model = "Some"
    speed = 123.5

    def __init__(self, wheels, model, speed):  # Метод для установки значений
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):  # Метод для вывода значений
        print("Автомобиль ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels,
              " колесах!")


ford = Car(4, "Ford", 60)
jeep = Car(4, "Jeep", 65)
ford.getAll()
jeep.getAll()


class Motocycle(Car):
    def __init__(self, wheels, model, speed, engine):
        super().__init__(wheels, model, speed)
        self.eng = engine

    def auto(self):
        print("Motocycle", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах",
              "c", "engine", self.eng)


Moto1 = Motocycle(2, "Honda", 150, 2.0)
Moto2 = Motocycle(2, "Harley Davidson", 200, "Powerfull!")
Moto1.auto()
Moto2.auto()


# 6

class Car:

    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def auto(self):
        print(x._wheels, x._model, x._speed)


x = Car(4, "Ford", 70)
x.auto()


# 7
class Car:
    wheels = 4
    model = "Some"
    speed = 123.5

    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        print("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")


A = Car(8, "Ford", 60)
B = Car(10, "Bus", 45)
A.getAll()
B.getAll()


# 8

class Car:
    wheels = 4
    model = "Some"
    speed = 123.5

    def __init__(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def set(self, wheels, model, speed):
        self.wheels = wheels
        self.model = model
        self.speed = speed

    def getAll(self):
        self.__protected()

    def __protected(self):
        print("Транспорт ", self.model, " может ехать со скоростью ", self.speed, " на всех ", self.wheels, " колесах!")


class Motorcycle(Car):
    engine = "Default"

    def __init__(self, wheels, model, speed, engine):
        super().__init__(wheels, model, speed)
        self.engine = engine

    def getAll(self):
        super().getAll()
        print("Его двигатель:", self.engine)

    def change(self):
        print("Двигатель мотоцикла установлен как: " + self.engine)


shkoda = Car(4, "Shkoda", 125.45)
shkoda.getAll()

audi = Car(4, "Audi", 250.9)
audi.getAll()

print("")  # Просто пропуск строки

harley = Motorcycle(2, "Harley Davidson", 200, "Powerfull")
harley.getAll()
harley.change()
