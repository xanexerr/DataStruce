class Student:
     class SportPlayer:
          def __init__(self, parent, sid):
               self.id = parent.id
               self.name = parent.name
               self.sid = sid
               
     def __init__(self, id, name):
          self.id = id 
          self.name = name
     
     def __str__(self):
     
          return f"Student {self.id} is {self.name}"

student = Student(1, 'Naphat')
guide = Student.SportPlayer(student, 1)
icq = Student(2, 'Kantinan')

std_list = [guide, icq]

# for i in std_list:
#      print(f"Student {i.id}  {i.name}",end=' ')
#      if hasattr(i, 'sid'):
#           print(f"is SportPlayer [SiD:{i.sid}] ")
#      else:
#           print()


class Car:
     def __init__(self, brand,model,year,color):
          self.brand = brand
          self.model = model
          self.year = year
          self.color = color
          
     def display(self):
          print(self.brand, self.model, self.year, self.color)
          
car1 = Car('Toyota', 'Altis', 2015, 'White')
car2 = Car('Honda', 'Civic', 2016, 'Black')
car3 = Car('Ford', 'Focus', 2017, 'Red')


# for i in [car1, car2, car3]:
#      i.display()    
     
# +