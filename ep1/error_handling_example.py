#handling simple error
# print(x)
print("Handling simple error")
try:
  print(x)
except:
  print("An exception occurred")

# #handling multiple error cases
print("Handling Multiple errors")
try:
  print("hi" + 3)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# #else keyword example
print("Handling errors with else keyword when no error foud ")
try:
  print(Hi)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# #fially keyword example
print("Handling errors with finally keyword")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# get type of exception
print("Get type of exception")
import sys

try:
  print("hi" + 10)
except:
   print("Oops!", sys.exc_info()[0], "occurred.")