# factorial calculation using recursion
def calculateFactorial(x):
    if x == 1:
        return 1
    else:
        return (x * calculateFactorial(x-1))
num = 20
facorial_number = calculateFactorial(num)
print("Factorial of ", num, "is 1 * 2 * 3 * 4 = ", facorial_number)