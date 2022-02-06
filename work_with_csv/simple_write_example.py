import csv
file = open("sample_data.csv", "r")
csvreader = csv.reader(file)
header = next(csvreader)
data = []
for row in csvreader:
    if(row[0] == 'Student 3'):
        row[2] = "Bangalore"
    data.append(row)

filename = 'simple_data_output.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data) # 5. write the rest of the data