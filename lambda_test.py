import boto3
import json
import os
def lambda_handler(event, context):
    # TODO implement
	ec2_client = boto3.client("ec2", region_name="us-west-2")
		
	reservations = ec2_client.describe_instances(Filters=[
			{
				"Name": "instance-state-name",
				"Values": ["running"],
			}
		]).get("Reservations")
		
	instances_list = []
		
	for reservation in reservations:
		for instance in reservation["Instances"]:
				instance_id = instance["InstanceId"]
				instance_type = instance["InstanceType"]
				public_ip = instance["PublicIpAddress"]
				private_ip = instance["PrivateIpAddress"]
				instances_list.append(instance_id)
				
				print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")
		
	return {
			'statusCode': 200,
			'body': json.dumps(instances_list)
	}

