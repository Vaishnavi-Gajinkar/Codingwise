""" Calculate the area & circumference of the shape """

class Shape:
    pi = 3.14               # class variable

    # def __init__(self,radius):
    #     self.radius = radius
        
    def circle(self, radius):
        self.radius = radius
        self.area = Shape.pi*radius*radius
        self.circumf = 2*Shape.pi*radius
        return self.area, self.circumf
    
    def square(self, edge=0):
        self.edge = edge
        self.area = edge**2
        self.circumf = 4*edge
        return self.area, self.circumf
    
    def rect(self,height=0,width=0):
        self.height = height
        self.width = width
        self.area = height * width
        self.circumf = 2*height + 2*width
        return self.area, self.circumf
    
accpt = input("Circle / Square / Rectangle \nEnter your preferred shape from above ")
s = Shape()

try:
    if accpt.lower() == 'circle':
        rad = float(input("Enter radius of circle "))
        area, circumference = s.circle(rad)
        print(f'With the given diamentions, \nArea is {area}sq units \nCircumference is {circumference} units')
    elif accpt.lower() == 'square':
        side = float(input("Enter length of one side of square "))
        area, circumference = s.square(side)
        print(f'With the given diamentions, \nArea is {area}sq units \nCircumference is {circumference} units')
    elif accpt.lower() == 'rectangle':
        len, breadth = [float(x) for x in input("Enter length and breadth value of rectangle (seperated by comma) ").split(',')]
        area, circumference = s.rect(len, breadth)
        print(f'With the given diamentions, \nArea is {area}sq units \nCircumference is {circumference} units')
    else:
        print("Invalid shape. Pls try again")
except:
    print("Something went wrong. Pls try again")
