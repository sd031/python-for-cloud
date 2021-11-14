#nested function example
def greet(name):
#here name is nonlocal variable
    def greetFirstName():
        # This is the nested function
        print("Hello ",name)

    greetFirstName()
    
greet("Sandip")