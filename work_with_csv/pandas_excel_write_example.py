import pandas as pd

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
data = pd.read_excel("./sample_data.xlsx")
print(data.columns)
#loop through column
# for itObj in data.Name:
#     print(itObj)
header = list(data.columns)
finalData = []

for index, row in data.iterrows():
    print("Name: "+row[0]+", Age: " + str(row[1]) + " Location: "+ row[2])
    if(row[0] == 'Student 3'):
        row[2] = "Bangalore"
    finalData.append(row)

rDataFrame = pd.DataFrame(finalData, columns=header)
with pd.ExcelWriter("samle_data_output.xlsx") as writer:
    rDataFrame.to_excel(writer, index=False) 