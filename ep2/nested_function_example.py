#nested function example
def greet(name):
    def greetFirstName():
        # This is the nested function
        print("Hello ",name)

    greetFirstName()
    
greet("Sandip")