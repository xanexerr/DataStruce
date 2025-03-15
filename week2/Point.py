class Point:
     def __init__(self, x, y, color="base"):
          self.x = x
          self.y = y
          self.color = color
     
     def __add__(self, other):
          new_color = self.color if self.color == other.color else self.color + "+" + other.color
          return Point(self.x + other.x, self.y + other.y, new_color)
     
     def __sub__(self, other):
          new_color = self.color if self.color == other.color else self.color + "-" + other.color
          return Point(abs(self.x - other.x), abs(self.y - other.y), new_color)
     
     def __mul__(self, other):
          new_color = self.color if self.color == other.color else "mixed"
          return Point(self.x * other.x, self.y * other.y, new_color)
     
     def __str__(self):
          return f"point({self.x}, {self.y}, {self.color})"

class Rectangle(Point):
     def __init__(self, x, y, width, height, color="base"):
          super().__init__(x, y, color)
          self.width = width
          self.height = height
     
     def __add__(self, other):
          return Rectangle(
               min(self.x, other.x),
               min(self.y, other.y),
               self.width+other.width ,
               max( self.height, other.height) ,
          )
     
     def __str__(self):
          return f"Rectangle(Point=({self.x}, {self.y}), width={self.width}, height={self.height}, color={self.color})"
     
     def area(self):
          return self.width * self.height

# Testing
print(":::Point:::")
p1 = Point(2, 3, "red")
p2 = Point(4, 5, "blue")
p3 = p1 + p2

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p1+p2 = {p3}")
print(f"p1-p2 = {p1-p2}")

print("\n:::Rectangle:::")
r1 = Rectangle(2, 3, 10, 20, "red")
print(f"R1 = {r1}")

r2 = Rectangle(4, 5, 5, 30, "blue")
print(f"R2 = {r2}")
r3 = r1 + r2
print(f"R3 width={r3.width}, height={r3.height}")
r2.x = (r1.x)+(r1.width)
print(f"New Position of R2 = {r2.x , r2.y}")
print(r2)