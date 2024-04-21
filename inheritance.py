class Car:
    price = 1000000

    def __init__(self, horsepower = 100):
        self.horsepower = horsepower

    def horse_powers(self):
        return f'У Car лошадиных сил {self.horsepower}'


class Nissan(Car):
    price = 7000000

    def horse_powers(self):
        print(f'У Nissan лошадиных сил {self.horsepower}')


class Kia(Car):
    price = 5000000

    def horse_powers(self):
        print(f'У Kia лошадиных сил {self.horsepower}')

niva = Car(100)
navara = Nissan(190)
stinger = Kia(370)
navara.horse_powers()
stinger.horse_powers()

print(niva.horse_powers())

print(niva.price)
print(navara.price)
print(stinger.price)
