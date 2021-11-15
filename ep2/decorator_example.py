#decorator example
def formatGreet(func):
    def innerfunc(name):
        print("***************")
        func(name)
        print("***************")
    return innerfunc
    
# def greetFirstName(name):
#         print("Hello ",name)


# prettyGreet = formatGreet(greetFirstName)
# prettyGreet("Sandip")

#or represent with @ as it's a syntactic sugar to implement decorators

@formatGreet
def greetFirstName(name):
        print("Hello ",name)

greetFirstName("Viewer")