# -*- coding: cp1251 -*-

class Transport:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Transport):
    
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
      
        
    def __str__(self):
        return "Марка: "+self.name+" Макс. скорость: "+str(self.max_speed)+" Пробег: "+str(self.mileage)
        
 
 
bus=Bus("Kamaz", 125, 12646)
print(bus)
print()





class Transport:

 def __init__(self, name, max_speed, mileage,):

  self.name = name

  self.max_speed = max_speed

  self.mileage = mileage

 def seating_capacity(self, capacity):

  return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):

  def seating_capacity(self, capacity = 50):

   return super ().seating_capacity(capacity = 50)

School_bus=Autobus("Kamaz", 125, 12646)

print(School_bus.seating_capacity())


