# # Принцыпы ООП
# # Наследование и Абстракция Инкапуляция и Полиформизом

# class Laptops:
#     def __init__(self, model, os, memory):
#         self.model = model#Бубличный отрибут
#         self._os = os#Зашишеный
#         self.__memory = memory#ПРиватный
#         #@ = декаратыр
#     @property
#     def memory(self):
#         return(self.__memory)


#     def info(self):
#         print(f"modek-{self.model}, {self._os}")
#         self._desrtop()
    
#     def _desrtop(self):
#         print("Рабочий стол")

#     def __password(self):
#         print("password = 1234")

#     @property
#     def password(self):
#         return self.__password

# huawei = Laptops("huawei", "Windows 11", 512)

# print(huawei.model)
# print(huawei._os)
# print(huawei.memory)
# huawei.info()
# # huawei.desrtop()
# huawei.password()







# import time
# def users(value):
#     def start():
#         print("Hello world!")
#         print(1)
#         value()
#         print("Bye!!")
#     return start

# @users
 
# def sey():
#     print("hy!")
# sey()

#Множественое наследовать

class Father:
    def __init__(self, name, age, beard):
        self.neme = name
        self.age = age
        self.beard = beard

    
    def work(self):
        print("Работает")



class Mother:
    def __init__(self, name, age, manikur):
        self.neme = name
        self.age = age
        self.manikur = manikur

    
    def cook(self):
        print("Гатовит")

class Child(Father, Mother):
    def __init__(self, name, age, beard, manikur, toys):
        Father.__init__(self, name, age, beard)
        Mother.__init__(self, name, age, manikur)
        self.toys = toys

        
    def cook(self):
        print("Я не у меню гатовит")

david = Child("David", 15, "ЧОрная борада", "Розовый маникур", "Много игрушек")
david.cook()
david.work()