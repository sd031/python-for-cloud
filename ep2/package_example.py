# import module from package
import Greeting.Person.greet
Greeting.Person.greet.say_hello()

#impport package as alias
import Greeting.Student.greet as greet_student
greet_student.say_hello()

#import module without package prefix
from Greeting.Patient import greet
greet.say_hello()

#import only function from package module
from Greeting.Patient.greet import say_welcome
say_welcome()