import pandas as pd
import json
# documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
data = pd.read_excel("./sample_data.xlsx")
#print headers 
print(data.columns)

for index, row in data.iterrows():
    print("Name: "+row[0]+", Age: " + str(row[1]) + " Location: "+ row[2])
