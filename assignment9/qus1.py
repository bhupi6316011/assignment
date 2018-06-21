''Ques 1 .Create a circle class and initialize it with radius.
 Make two methods getArea and getCircumference inside this class.'''



class Circle:


    radius=10
    def getArea(self):

        b = 3.14 * self.radius * self.radius
        print("Area of Circle is: ",b)
    def getCircumference(self):

        b = self.radius * 2 * 3.14
        print("Circumference of circle is :",b)


b1=Circle()
b1.getArea()
b1.getCircumference()
