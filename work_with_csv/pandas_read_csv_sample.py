import pandas as pd

#more documentation https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = pd.read_csv("./sample_data.csv",  delimiter=',')
#print headers 
print(data.columns)
#print particular column
print(data.Name)
print(data.Age)
print(data.Location)
#loop through column
# for itObj in data.Name:
#     print(itObj)

for index, row in data.iterrows():
    print("Name: "+row[0]+", Age: " + str(row[1]) + " Location: "+ row[2])
