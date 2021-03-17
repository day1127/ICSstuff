import math



class Circle:

    def __init__(self, radius, x = 0, y = 0):

        self.radius = radius

        self.x = x

        self.y = y



    def __str__(self):

        return f"{self.x}, {self.y}, radius = {self.radius}"



    def area(self):

        return math.pi * self.radius**2



    def printArea2(self):

        print(round(self.area(), 2))










class Rectangle:

    def __init__(self, x, y, width, height):

        self.x = x
        self.y = y
        self.width = width
        self.height = height



    def __str__(self):
        return f"The dimensions of your rectangle are x= {self.x}, y= {self.y}, width = {self.width}, hight = {self.height}"






    def area(self):
        return f"The area is {self.width * self.height} "
