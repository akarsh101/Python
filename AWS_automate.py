#MIT License
#
#Copyright (c) 2021 Maddipati Venkata Akarsh
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import boto3
import os
from botocore.exceptions import ClientError
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
os.environ['AWS_ACCESS_KEY_ID'] = input("ENTER AWS ACCESS KEY ID:\n")
os.environ['AWS_SECRET_ACCESS_KEY'] = input('ENTER AWS SECRET ACCESS KEY:\n')
os.environ['AWS_SESSION_TOKEN']=input('ENTER AWS SESSION TOKEN:\n')
boto3.setup_default_session()
# Option 1: S3 client list of buckets with name and is creation date
s3 = boto3.client('s3')
response = s3.list_buckets()['Buckets']
print("\nNumber of S3 buckets Running are: ",len(s3.list_buckets()['Buckets']))
for bucket in response:
    print('\nBucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))
#EC2 instances region, no of running instances and Reservation Description
i=0
regions= [
    #'ap-east-1',
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-south-1',
    'ap-southeast-1',
    'ap-southeast-2',
    'ca-central-1',
    'eu-central-1',
    'eu-north-1',
    'eu-west-1',
    'eu-west-2',
    'eu-west-3',
    #'me-south-1',
    'sa-east-1',
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2'
    ]

for region_name in regions:
    ec2= boto3.resource('ec2', region_name=region_name)
    instances= ec2.meta.client.describe_instances()
    #for instance in instances['']:
    if instances['Reservations']:
        print(f'\nregion_name: {region_name}\n')
        if region_name:
            i=i+1
        print("No of regions the instances are running: ",i)
        print("\n",instances)
