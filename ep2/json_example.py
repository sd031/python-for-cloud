
#parsing JSON data: Converting JSON string to Python Dictionary
import json
person_json =  '{ "name":"Sandip", "age":30, "city":"Kolkata"}'
# parse x:
person_object = json.loads(person_json)
print("Peron's age is: ",person_object["age"])


#converting Python Dictionary to JSON string
person_object["age"] = 45
new_person_json = json.dumps(person_object)
print("New Person JSON string: ", new_person_json)
print("Data type of JSON Dump",  type(json.dumps(new_person_json)))

# a complete json example with different data type
import json

x = {
  "name": "Sandip Das",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Coming soon",),
  "pets": None,
  "cars": [
    {"model": "Maruti Dzire"},
  ]
}

print("JSON example with different data type: ",json.dumps(x))
print("Data type of JSON Dump",  type(json.dumps(x)))