# Implicit Type Conversion
numerInt = 123
numberFloat = 1.23

numNew = numerInt + numberFloat

print("datatype of numerInt:",type(numerInt))
print("datatype of numberFloat:",type(numberFloat))

print("Value of numNew:",numNew)
print("datatype of numNew:",type(numNew))

#explicit type conversion

numerInt = 123
numStr = "456"

print("Data type of numerInt:",type(numerInt))
print("Data type of numStr before Type Casting:",type(numStr))

numStr = int(numStr)
print("Data type of numStr after Type Casting:",type(numStr))

numSum = numerInt + numStr

print("Sum of numerInt and numStr:",numSum)
print("Data type of the sum:",type(numSum))