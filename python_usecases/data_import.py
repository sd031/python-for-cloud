import requests
import json
from google.cloud import bigquery
# import boto3
# response_API = requests.get('https://gmail.googleapis.com/$discovery/rest?version=v1')
# # print(response_API.text)
# data = response_API.text
# parsed_json_dictionary = json.loads(data)

# #got the data
# print(parsed_json_dictionary["resources"]["users"]["methods"]["getProfile"]["scopes"][0])



client = bigquery.Client()

QUERY = (
    'SELECT name FROM `bigquery-public-data.usa_names.usa_1910_2013` '
    'WHERE state = "TX" '
    'LIMIT 100')
query_job = client.query(QUERY)  # API request
rows = query_job.result()  # Waits for query to finish
for row in rows:
    print(row.name)