import csv
#open the file in read mode
file = open("./sample_data.csv")
# The type is _io.TextIOWrapper
# print(type(file)) 
#read parse the csv file
csvreader = csv.reader(file)
#next() method to get header , nex time calling will retrurn next row
header = next(csvreader)
print(header)
# defining blank rows list/array variable 
rows = []
#iterating over csvreader rows
for row in csvreader:
    print(row[2])
    rows.append(row)
#pirnt final rows
# print(rows)
file.close()