# # SuperCar = Верблюжий регис

# # super_car= Змеиный регистр


# class Car:# Чертеж или же шаблон
#     wheels = 4 #Атребут\Поле\Свойства класс
#     def __init__(self, model, color):# ЭТО сам объект INIt это канструктор
#         self.model = model
#         self.color = color
#         self.is_start = False

    
#     def info(self):
#         print(f"Model - {self.model}, color - {self.color}")

#     def start(self):
#         self.is_start = True
#         print(f"Мошинав {self.model} завелас")
    
#     def drive(self):
#         if self.is_start == True:
#             print(f"Мошина {self.model} поехала")
#         else:
#             print(f"Машина {self.model} не заведена")
#     def stop(self):
#         self.is_start = False
#         print(f"Машина {self.model} заглушена")

# super_car = Car("Mersedes - cls", "black") #Объект класса
# super_car_2 = Car("BMW - m5", "white")
# # print(super_car.wheels)
# # print(super_car.model)
# # print(super_car_2.wheels)
# # print(super_car_2.model)
# super_car.info()
# print(super_car.is_start)
# super_car.drive()
# print(super_car.is_start)
# super_car.start()
# print(super_car.is_start)
# super_car.drive()
# super_car.stop()
# super_car_2.info()








class Test:
    def print_text(self):
        print("это дочерный класс (Test)")


class Test2:
    def print_text(self):
        print("это дочерный класс (Test2)")

test = Test2()
test.print_text()