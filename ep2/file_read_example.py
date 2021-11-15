#File read example
#Simple Read file example
# f = open("sample_file.txt", "r")
# print(f.read())
# f.close()

#read file by full path
# f = open("/Users/sandipdas/python-for-cloud/ep2/sample_file.txt", "r")
# print(f.read())
# f.close()

#we can read file with speific encding
# f = open("sample_file.txt", mode='r', encoding='utf-8')
# print(f.read())
# f.close()

#loop  through the file lines
f = open("sample_file.txt", "r")
# for x in f:
#   print("line: ",x)
# f.close()

#read file is the file exists
import os
if os.path.exists("sample_file.txt"):
    f = open("sample_file.txt", "r")
    print(f.read())
    f.close()
else:
  print("The file does not exist")