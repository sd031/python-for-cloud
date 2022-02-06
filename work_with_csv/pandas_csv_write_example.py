import pandas as pd
import json

#more documentation https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
data = pd.read_csv("./sample_data.csv",  delimiter=',')
print(data.columns)
#loop through column
# for itObj in data.Name:
#     print(itObj)
header = data.columns
finalData = []

for index, row in data.iterrows():
    print("Name: "+row[0]+", Age: " + str(row[1]) + " Location: "+ row[2])
    if(row[0] == 'Student 3'):
        row[2] = "Bengalore"
    finalData.append(row)

rDataFrame = pd.DataFrame(finalData, columns=header)
rDataFrame.to_csv('sample_data_by_pandas.csv', index=False)


