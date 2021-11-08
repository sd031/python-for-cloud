name = "Sandip Das"
print(type(name)) 

#check strig length
print(len(name))


# multilie string
a = """This is,
a 
multi line
strig 1"""
print(a)

a = '''This is,
a 
multi line
strig 2'''
print(a)

#format variables in string

age = 30
txt = "My name is Sadip, and I am {}"
print(txt.format(age))

quantity = 14
itemNo = 456
price = 199.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemNo, price))

#via index
quantity = 14
itemNo = 456
price = 199.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemNo, price))
