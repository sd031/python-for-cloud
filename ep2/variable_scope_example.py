#global scope example
# x = "I am a Global Variable"
# def someFunction():
#     print("x inside function:", x)
# someFunction()
# print("x outside function:", x)


# Global Scope conflict reslution: Treating global and local variables as different variable name

# x = "I am a Global Variable"
# def someFunction():
#     x = "I am a Local Variable"
#     print("x inside function:", x)
# someFunction()
# print("x outside function:", x)

# Global valiable using global keyword
# def someFunction():
#   global x
#   x = 500
#   print("x inside function:", x)
# someFunction()
# print("x outside function:", x)



#local scope example
# def someSimpleFunction():
#   x = 500
#   print("x inside function:", x)
# someSimpleFunction()
#error will be raised as x is not defined in global scope
#print("x outside function:", x)

#nonlocal variable example
def outerFunction():
    x = "I am local value"
    def innerFuntion():
        nonlocal x
        x = "I am non-local value"
        print("inner function value of x:", x)
    innerFuntion()
    print("outer function value of x:", x)
outerFunction()