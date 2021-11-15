#defining a class
# class MySimpleClass:
#  x = 20
#  def printValueOfX(self):
#       print('Value of x is ', self.x)

# creating an object from a class
# c = MySimpleClass()
# c.printValueOfX()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greetPerson(self):
        print("Hello " + self.name)
        print("Your age is " , self.age)
        

p = Person("John", 36)
p.greetPerson()







# Note
# An object is a fundamental building block of an object-oriented language. 
# Integers, strings, floating point numbers, even arrays and dictionaries, 
# are all objects. More specifically, any single integer or any single string 
# is an object. The number 12 is an object, the string "hello, world" is an object, 
# a list is an object that can hold other objects, and so on. You've been using 
# objects all along and may not even realize it.