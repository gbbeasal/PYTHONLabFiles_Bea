import logging, os
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


def create_tempfile(file_name=None, content=None, size=300):
#Create a temporary text file
    filename = f'{file_name or uuid.uuid4().hex}.txt'
    
    with open(filename, 'w') as f:
        f.write(f'{(content or "0") * size}')
    return filename


def create_bucket_object(bucket_name, file_path, key_prefix=None):
    file_path = os.getcwd()+'/'+f'{filename}'
    bucket = get_bucket('bucketnibea')
    dest = f'{key_prefix or ""}{file_path}'
    bucket_object = bucket.Object(dest)
    bucket_object.upload_file(Filename=file_path)
    return bucket_object