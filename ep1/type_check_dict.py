person = {
"name": "Sandip",
"age": 30,
"location" : "Kolkata"
}
print(type(person))
print(type(person['name']))
print(type(person["age"]))

#get values in disctionary by key
print(person["name"])

# We can check key of a dictionary using the in keyword
print("name" in person)

#chage value of a dictionary
person["age"] = 31
print(person["age"])

person.update({"age": 29})
print(person["age"])

#addig value of a dictionary
person["eye_color"] = "brown"
print(person)

person.update({"hair_color": "black"})
print(person)

#delete particular key from dictionary
person.pop("hair_color")
print(person)

#delete last item from dictionary
person.popitem()
print(person)

#delete particular key from dictionary usig del keyword
del person["age"]
print(person)

#empty dictionary usig clear method
person.clear()
print(person)

person = {
"name": "Sandip",
"age": 30,
"location" : "Kolkata"
}
#Loop dictionary
for x in person:
  print("key: ",x)
  print("value: ",person[x])

#Loop dictionary key 
for x in person.keys():
  print("Key",x)

#Loop dictionary value
for x in person.values():
  print("Value",x)

#Loop dictionary key and value
for x,y in person.items():
  print(x,y)


