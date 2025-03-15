class Animal:
     def __init__(self, name):
         self.name = name
     
     def speak(self):
         return print("make a sound")

class Dog(Animal):
     def speak(self):
         return f"{self.name} says Woof!"
    
class Cat(Animal):
     def speak(self):
         return f"{self.name} says Meow!"

Dog1 = Dog("Si")
Cat1 = Cat("Jimjum")

print(Dog1.speak())
print(Cat1.speak())

class Vehicle:
     def __init__(self, brande,model):
           self.brand = brande
           self.model = model
           
     def details(self):
          return f"{self.brand} {self.model}"

class Car(Vehicle):
     def __init__(self, brand, model, year):
          super().__init__(brand, model)
          self.year = year
          
          
     def details(self):
          return f"{self.year} {self.brand} {self.model} {self.year}"
     
class ElectricCar(Car):
     def __init__(self, brand, model, year, battery):
          super().__init__(brand, model, year)
          self.battery = battery
          
     def details(self):
               return f"{self.year} {self.brand} {self.model} {self.year} {self.battery}"
          
verhicle = Vehicle("General", "Motors")
car = Car("Toyota", "Altis", 2015)
electricPcar = ElectricCar("Tesla", "Model S", 2019, "100kWh")

print(verhicle.details())
print(car.details())
print(electricPcar.details())