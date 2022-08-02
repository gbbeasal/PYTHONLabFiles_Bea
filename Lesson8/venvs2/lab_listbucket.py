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

def list_buckets():
    s3 = boto3.resource('s3')
    
    count = 0
    for bucket in s3.buckets.all():
        print(bucket.name)
        count += 1
    
    print(f'Fount {count} buckets!!')

list_buckets()