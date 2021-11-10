# normal while loop example
# print("Normal While Loop example")
# i = 0
# while i < 10:
#   print(i)
#   i += 1

#break statement example for while loop
# print("break statement example for while loop")
# i = 1
# while i < 10:
#   print(i)
#   if i == 5:
#     break
#   i += 1

# #continue statement example for while loop
print("continue statement example for while loop")
i = 0
while i < 10:
  i += 1
  if i == 5:
    continue
  print(i)


# #else statement example for while loop
print("else statement example for while loop")

i = 0
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")