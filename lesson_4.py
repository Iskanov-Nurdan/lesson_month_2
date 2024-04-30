class ElectroCar:
    def __init__(self, power, battery):
        self.power = power
        self.battery = battery

    def info(self, value):
        print(f"Мощьность: {self.power},vat \n Заряд ботереи: {self.battery} mah = {value}")
    
    def __repr__(self):# repr == print
        return f"Мощьность: {self.power},vat \n Заряд ботереи: {self.battery} mah"

    def __str__(self):# str == print
        return f"Мощьность: {self.power},vat \nЗаряд ботереи: {self.battery} mah - Это метот str"

    def __call__(self):
        print("Hello world")

    # Магические методы для арифмитеических действии    
    
    def __add__(self, other): #add + 
        new_power = self.power + other.power
        return ElectroCar(new_power, self.battery)

    def __sub__(self, other): #add -
        new_power = self.power - other.power
        return ElectroCar(new_power, self.battery)

    def __mul__(self, other): #add * 
        new_power = self.power * other.power
        return ElectroCar(new_power, self.battery)

    def __truediv__(self, other): #add / 
        new_power = self.power / other.power
        return ElectroCar(new_power, self.battery)

    
    def __floordiv__(self, other): #add / 
        new_power = self.power // other.power
        return ElectroCar(new_power, self.battery)

    # Магические методы для оперетора соавнение
    def __gt__(self, other): # >
        return self.battery > other.battery

    def __lt__(self, other): # <
        return self.battery < other.battery

    def __eq__(self, other): # =
        return self.battery == other.battery

    def __ne__(self, other): # !=
        return self.battery != other.battery

    def __ge__(self, other): # >=
        return self.battery >= other.battery

    def __le__(self, other): # <=
        return self.battery <= other.battery




car = ElectroCar(999, 20000)
car_2 = ElectroCar(999, 20000)

print(car + car_2)
print(car - car_2)
print(car * car_2)
print(car / car_2)
print(car // car_2)
# car.info(12)
print(car)
# print("Hello world")
# car(2, 4)

    # Магические методы для оперетора соавнение
print(car > car_2)
print(car < car_2)
print(car == car_2)
print(car != car_2)
print(car >= car_2)
print(car <= car_2)


