import logging
import random
import uuid
from datetime import datetime
from decimal import Decimal
from pathlib import Path, PosixPath

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s',
)
log = logging.getLogger()

def create_bucket(name, region=None):
    region = region or 'us-east-2'
    client = boto3.client('s3', region_name=region)
    params = {
        'Bucket': name, 
        'CreateBucketConfiguration': {
            'LocationConstraint': region,
        }
    }
    
    try:
        client.create_bucket(**params)
        return True
    except ClientError as err:
        log.error(f'{err} - Params {params}')
        return False

###All False bc these buckets exist! Buckets must be globally unique
#create_bucket('tesr')
#print(create_bucket('testawesomeproject2'))
#print(create_bucket('testawesomeproject3'))

#print(create_bucket('bucketnibea')) #returns True because this is a non-existent bucket before.

#use test_boto3.py to check if bucket has been created.