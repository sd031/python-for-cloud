#parent or base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greetPerson(self):
        print("Hello " + self.name)

#child / derived class

# class Patient(Person):
#   def __init__(self, name, age, case):
#         Person.__init__(self, name, age)
#         self.case = case
#   def print_case(self):
#         print("Patient's case is " + self.case)

# patientObject = Patient("John", 30, "cold")
# patientObject.greetPerson()
# patientObject.print_case()

# Using super() function, we do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent. 

class Patient(Person):
  def __init__(self, name, age, case):
    super().__init__(name, age)

newParient = Patient("John", "Doe", "Fever")
newParient.greetPerson()


