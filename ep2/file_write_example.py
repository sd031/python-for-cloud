
# append mode 
# f = open("sample_file_2.txt", "a")
# f.write("This is a line added by python function\n")
# f.close()

#just read the recently added line
# f = open("sample_file_2.txt", "r")
# print(f.read())
# f.close()


#file write mode example
f = open("sample_file_2.txt", "w")
f.write("This is a line just overwritten the existing file\n")
f.close()
f = open("sample_file_2.txt", "r")
print(f.read())
f.close()