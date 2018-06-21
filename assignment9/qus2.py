'''Ques 2. Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.'''


class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def show(self):
        print(self.name,self.roll)
s1=Student("Bhupi",6316011)
s1.show()