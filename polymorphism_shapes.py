#Polymorphism

welcome='<<<<<-----Welcome to the Area Calculator ----->>>>>'
print(welcome.upper())
class Area():

    def __init__(self,length,breadth,radius):
        self.length=length
        self.breadth=breadth
        self.radius=radius

    def square_area(self):
        return self.length*self.length
    
    def rectangle_area(self):
        return self.breadth*self.length
    
    def circle_area(self):
        return 3.1415*(self.radius*self.radius)
    
length=float(input('Enter the required length (in m)-->'))
breadth=float(input('Enter the required breadth (in m )-->'))
radius=float(input('Enter the required radius (in m)-->'))    
    
sq=Area(length,breadth,radius)
rec=Area(length,breadth,radius)
cir=Area(length,breadth,radius)
    
print(f'The area of square is {sq.square_area()} sq.m having length of {length} m')    
print(f'The area of rectangle is {rec.rectangle_area()} sq.m having length of {length} m and breadth of {breadth} m')
print(f'The area of the circle is  {cir.circle_area()} sq.m having the radius of {radius} m.')

