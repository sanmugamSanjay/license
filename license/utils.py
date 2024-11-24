import frappe
import boto3
import json
from uptime_kuma_api import UptimeKumaApi, MonitorType
# from botocore.exceptions import ClientError

def get_uptime_kuma():
    # api_key=frappe.conf.get("uptime_key")
    client = UptimeKumaApi('http://192.168.2.49:3001/')
    client.login('velavan', 'Aalam@123')
    return client

def create_aws_client(service, aws_access_key, aws_secret_key, region):
    """
    Create a boto3 client for the specified AWS service.
    """
    return boto3.client(
        service,
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )

def get_ec2_details(ec2_client):
    """
    Fetch EC2 instance details and return them as a JSON object.
    """
    ec2_instances = []
    try:
        ec2_response = ec2_client.describe_instances()
        for reservation in ec2_response['Reservations']:
            for instance in reservation['Instances']:
                instance_details = {
                    "name": instance['InstanceId'],
                    "instanceid": instance['InstanceId'],
                    "state": instance['State']['Name'],
                    "publicip": instance.get('PublicIpAddress', 'N/A'),
                    "privateip": instance.get('PrivateIpAddress', 'N/A'),
                    "launchtime": str(instance['LaunchTime']),
                    "instancetype": instance['InstanceType'],
                    "availabilityzone": instance['Placement']['AvailabilityZone']
                }
                ec2_instances.append(instance_details)
    except ClientError as e:
        print(f"Error fetching EC2 details: {e}")
    return ec2_instances
