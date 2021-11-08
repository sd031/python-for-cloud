# Implicit Type Conversion
numerInt = 123
numberFloat = 1.23

num_new = numerInt + numberFloat

print("datatype of numerInt:",type(numerInt))
print("datatype of numberFloat:",type(numberFloat))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#explicit type conversion

numerInt = 123
num_str = "456"

print("Data type of numerInt:",type(numerInt))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = numerInt + num_str

print("Sum of numerInt and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))