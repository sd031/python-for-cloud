import os
import logging
import json
import boto3
from botocore.exceptions import ClientError
from boto3.s3.transfer import TransferConfig
import requests

bucket_name = "sandip-boto3-live-demo-bucket"
region_name = "us-west-2"

def create_bucket(bucket_name, region=None):
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
#create_bucket(bucket_name, region_name)


def list_buckets( region=None):
    # Create bucket
    s3_client = boto3.client('s3')
    try:
        if region is not None:
            s3_client = boto3.client('s3', region_name=region)
        response = s3_client.list_buckets()
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')
    except ClientError as e:
        logging.error(e)
        return False
    return True

#list_buckets(region_name)

def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file("./sample_file_1.txt", bucket_name, "sample_file_1.txt")

def upload_file_object(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        with open(file_name, "rb") as f:
            s3_client.upload_fileobj(f, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file_object("./sample_file_2.txt", bucket_name, "sample_file_2.txt")

#create_bucket("eampty-bucket-example-sandip", region_name)
def delete_empty_bucket(bucket):
    s3_client = boto3.client('s3')
    response = s3_client.delete_bucket(Bucket=bucket)
    print(response)
#delete_empty_bucket(bucket_name)

def delete_non_empty_bucket(bucket):
    s3_client = s3 = boto3.resource('s3') 
    bucketClient = s3_client.Bucket(bucket)
    bucketClient.objects.all().delete()
    bucketClient.meta.client.delete_bucket(Bucket=bucket)
#delete_non_empty_bucket(bucket_name)
def delete_object(bucket,object_name):
    s3_client = boto3.client('s3')
    response = s3_client.delete_object(Bucket=bucket,Key=object_name)
    print(response)
# delete_object(bucket_name, "sample_file_2.txt")

# downloaded_files
def download_file(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
download_file("./downloaded_files/sample_file_1.txt", bucket_name, "sample_file_1.txt")

def download_file_object(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        with open(file_name, "wb") as f:
            s3_client.download_fileobj(bucket, object_name, f)
    except ClientError as e:
        logging.error(e)
        return False
    return True
download_file_object("./downloaded_files/sample_file_2.txt", bucket_name, "sample_file_2.txt")

def upload_file_multipart(file_name, bucket, object_name=None):
    #upload_file transfer to be multipart if the file size is larger 
    #than the threshold specified in the TransferConfig object.
    GB = 1024 ** 3
    config = TransferConfig(multipart_threshold=5*GB)

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, Config=config)
    except ClientError as e:
        logging.error(e)
        return False
    return True
# upload_file_multipart("./sample_file_1.txt", bucket_name, "sample_file_1.txt")

def download_file_concurrently(file_name, bucket, object_name):
    #default concurrency is 10
    config = TransferConfig(max_concurrency=20)
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket, object_name, file_name,Config=config)
    except ClientError as e:
        logging.error(e)
        return False
    return True
# download_file_concurrently("./downloaded_files/sample_file_1.txt", bucket_name, "sample_file_1.txt")

def create_presigned_url(bucket, object_name, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket,
            'Key': object_name},
            ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response

# responseObject = create_presigned_url(bucket_name,"sample_file_1.txt")
# print(responseObject)

def create_presigned_upload_url(bucket_name, object_name,
                          fields=None, conditions=None, expiration=3600):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response

# uplodable_file_name = "./sample_file_3.txt"
# uploadOject = create_presigned_upload_url(bucket_name,"sample_file_3.txt")
# print(uploadOject)
# with open(uplodable_file_name, 'rb') as f:
#     files = {'file': (uplodable_file_name, f)}
#     http_response = requests.post(uploadOject['url'], data=uploadOject['fields'], files=files)
# #If successful, returns HTTP status code 204
# print(f'File upload HTTP status code: {http_response.status_code}')

def change_object_permission(bucket, object_name, permission):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.put_object_acl(Bucket=bucket, 
                  Key=object_name, 
                  ACL=permission)
    except ClientError as e:
        logging.error(e)
        return None
    return response

change_object_permission(bucket_name, "sample_file_3.txt", "private")