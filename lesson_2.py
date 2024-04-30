
#Принцыпы ООП
#Наследование и Абстракция и Полиформизом



# class Peaple:#Абстрактный класс и Родительский класс
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Parents(Peaple):#Родительский класс

#     def info(self):
#         print(f" имя {self.name}, возраст {self.age}")

#     def swim(self):
#         print(" Я не умею пловать")

# mother = Parents("Nagima", 41)
# mother.info()
# mother.swim()

# class Children(Parents):
#     def __init__(self, name, age, property):
#         super().__init__(name, age)
#         self.property = property

#     def swim(self):
#             print("Я умею пловать")

# child = Children("Alihan", 15, 0)
# child.info()
# child.swim()
    


# class Animals:
#     def __init__(self, name, eyes):
#         self.name = name
#         self.eyes = eyes

#     def make_sound():
#         pass

# class Dogs(Animals):
#     def make_sound(self):
#         print("Gaf-Gaf")

# class Cats(Animals):
#     def make_sound(self):
#         print("Meow")

# class Fish(Animals):
#     def make_sound(self):
#         print("bul-bul")

# dog = Dogs("Sharik", "Карие")
# cat = Cats("Murka", "Зеленые")
# fish = Fish("Nemo", "Оронживый")

# dog.make_sound()
# cat.make_sound()
# fish.make_sound()