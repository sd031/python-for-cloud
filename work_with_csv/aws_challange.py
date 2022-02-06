import pandas as pd
import boto3
from botocore.exceptions import ClientError

data = pd.read_csv("./aws_s3_input.csv",  delimiter=',')
print(data.columns)
header = data.columns
finalData = []

bucket = 'python-aws-challenge'
s3_client = boto3.client('s3')

for index, row in data.iterrows():
    object_name = row[1] 
    try:
     response = s3_client.delete_object(Bucket=bucket,Key=object_name)
     statusCode = response["ResponseMetadata"]["HTTPStatusCode"]
     row[2] = "Deleted ("+ str(statusCode) + ")"
    except ClientError as e:
     row[2] = "Not Deleted"
     print(e)
    finalData.append(row)

rDataFrame = pd.DataFrame(finalData, columns=header)
rDataFrame.to_csv('aws_s3_result.csv', index=True)