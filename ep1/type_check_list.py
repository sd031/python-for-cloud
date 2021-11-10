simpleList = ["red", "green", "blue", 4, 5, 6]
print(simpleList)
print(type(simpleList))

#simpleList[1] = green type is str 
print("simpleList[1] = ", simpleList[1])

print(type(simpleList[1]))

#simpleList[4] = 5 type is int 
print("simpleList[4] = ", simpleList[4])

print(type(simpleList[4]))

# simpleList[0:3] = ['red', 'green']
print("simpleList[0:3] = ", simpleList[0:3])

# simpleList[3:] = [4, 5, 6]
print("simpleList[3:] = ", simpleList[3:])

# chagig value of item in list
simpleList[2] = 3
print("value did changed", simpleList)

# get last value of list
print("simpleList[-1] = ", simpleList[-1])

#we can add value to list
simpleList.insert( 6,"new value")
print("New item added to list",simpleList)

#we can remove value from list by item value
simpleList.remove( "new value")
print("one item removed from list by value",simpleList)

#we can remove value from list by item index
simpleList.pop(2)
print("one item removed from list by index", simpleList)

#we can run for loop on list
for x in simpleList:
  print(x)






