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
        

def list_buckets():
    s3 = boto3.resource('s3')
    count = 0
    for bucket in s3.buckets.all():
        print(bucket.name)
        count += 1
    print(f'Found {count} buckets!')


def get_bucket(name, create=False, region=None):
    client = boto3.resource('s3')
    bucket = client.Bucket(name=name)
    if bucket.creation_date:
        return bucket
    else:
        if create:
            create_bucket(name, region=region)
            return get_bucket(name)
        else:
            log.warning(f'Bucket {name} does not exist!')
            return


def create_tempfile(file_name=None, content=None, size=300):
#Create a temporary text file
    filename = f'{file_name or uuid.uuid4().hex}.txt'
    
    with open(filename, 'w') as f:
        f.write(f'{(content or "0") * size}')
    return filename


def create_bucket_object(bucket_name, file_path, key_prefix=None):
    file_path = os.getcwd()+'/'+f'{filename}'
    bucket = get_bucket('testawesomeproject4-bea')
    dest = f'{key_prefix or ""}{file_path}'
    bucket_object = bucket.Object(dest)
    bucket_object.upload_file(Filename=file_path)
    
    return bucket_object


def get_bucket_object(bucket_name, object_key, dest=None, version_id=None):
    bucket = get_bucket(bucket_name)
    params = {'key': object_key}
    if version_id:
        params['VersionId'] = version_id
    bucket_object = bucket.Object(**params)
    dest = Path(f'{dest or ""}')
    file_path = dest.joinpath(PosixPath(object_key).name)
    bucket_object.download_file(f'{file_path}')
    return bucket_object, file_path


def main():
    print("1. CREATING BUCKETS: ")
    create_bucket('testawesomeproject4-bea', region=None)
    print("\n\n 2. LISTING BUCKETS: ")
    list_buckets()
    
    

if __name__ == '__main__':
    main()
    print(f'\n\n 3. GETTING BUCKETS : ')
    cdate = get_bucket('testawesomeproject4-bea').creation_date
    print('Bucket Creation Date :', cdate)
    filename = create_tempfile()
    b_obj = create_bucket_object('testawesomeproject4-bea', filename, key_prefix='temp/')
    
    print("\n\n 4. CREATING BUCKET OBJECT AND KEY ")
    print("Bucket Object: ", b_obj)
    print("Bucket Object Key: ", b_obj.key)
    
    print("\n\n 5. GETTING BUCKET OBJECT :")
    
    