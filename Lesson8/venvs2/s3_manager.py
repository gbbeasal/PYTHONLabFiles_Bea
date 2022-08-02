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
#//

def create_tempfile(file_name=None, content=None, size=300):
#Create a temporary text file
    filename = f'{file_name or uuid.uuid4().hex}.txt'
    
    with open(filename, 'w') as f:
        f.write(f'{(content or "0") * size}')
    return filename


def create_bucket_object(bucket_name, file_path, key_prefix=None):
    file_path = os.getcwd()+'/'+f'{tmp_file}'
    bucket = get_bucket('testing-bea')
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


def enable_bucket_versioning(bucket_name):
    #Enable bucket versioning for the given bucket_name
    
    bucket = get_bucket(bucket_name)
    versioned = bucket.Versioning()
    versioned.enable()
    return versioned.status


def delete_bucket_objects(bucket_name, key_prefix=None):
    bucket = get_bucket(bucket_name)
    objects = bucket.object_versions
    if key_prefix:
        objects = objects.filter(Prefix=key_prefix)
    else:
        objects = objects.iterator()
    targets = [] # This should be a max of 1000
    for obj in objects:
        targets.append({
            'Key': obj.object_key,
            'VersionId': obj.version_id,
    })
    bucket.delete_objects(Delete={
        'Objects': targets,
        'Quiet': True,
    })
    return len(targets)


def delete_buckets(name=None):
    count = 0
    if name:
        bucket = get_bucket(name)
        if bucket:
            bucket.delete()
            bucket.wait_until_not_exists()
            count += 1
    else:
        count = 0
        client = boto3.resource('s3')
        for bucket in client.buckets.iterator():
            try:
                bucket.delete()
                bucket.wait_until_not_exists()
                count += 1
            except ClientError as err:
                log.warning(f'Bucket {bucket.name}: {err}')
    return count


def main():
    print("1. CREATING BUCKETS: ")
    list_buckets()
    create_bucket('testing-bea', region=None)
    print("\n\n 2. LISTING BUCKETS: ")
    list_buckets()
    
    

if __name__ == '__main__':
    main()
    print(f'\n\n 3. GETTING BUCKETS : ')
    cdate = get_bucket('testing-bea').creation_date
    print('Bucket Creation Date :', cdate)
    tmp_file = create_tempfile()
    b_obj = create_bucket_object('testing-bea', tmp_file, key_prefix='temp/')
    
    print("\n\n 4. CREATING BUCKET OBJECT AND KEY :")
    print("Bucket Object: ", b_obj)
    print("Bucket Object Key: ", b_obj.key)
    
    print("\n\n 5. GETTING BUCKET OBJECT :")
    tmp_file = Path(tmp_file)
    tmp_file.unlink()
    bucket_obj_key = b_obj.key
    b_obj, tmp_file = get_bucket_object('testing-bea',bucket_obj_key)
    print("Downloaded Bucket Object: ", b_obj)
    print("Object Key of downloaded bucket object: ", b_obj.key)
    
    print("\n\n 6. CREATE BUCKET OBJECT VERSION :")
    enable_bucket_versioning('testing-bea')
    # Shows contents of the object key txt file:
    print("Contents of the Object Key text file: ", tmp_file.open().read())
    # Editing the contents:
    tmp_file.open(mode='w').write('10' * 500)
    print("Contents of the OBject Key text file: ",tmp_file.open().read())
    
    print("\n\n 7. UPLOADING FILE TO THE SAME BUCKET OBJECT :")
    create_bucket_object('testing-bea', tmp_file.name, key_prefix='temp/')
    p1 = list(get_bucket('testing-bea').objects.all())
    print("All bucket object latest versions: ", p1)
    p2 = list(get_bucket('testing-bea').object_versions.all())
    print("\nAll bucket object versions: ", p2)
    
    print("\n\n 8. FILTERING BUCKET OBJECT :")
    # First let's create other objects in the bucket
    for _ in range(3):
        obj = create_bucket_object(
        'testing-bea',
        file_path=create_tempfile(),
        key_prefix='others/'
        )
        print(f'Object {obj.key} created!')
    p3 = list(get_bucket('testing-bea').objects.all())
    print("\nAll bucket object latest version: ", p3)
    p4 = list(get_bucket('testing-bea').objects.filter(Prefix='temp/'))
    print("\nAll bucket object latest version - Filtered: ", p4)
    
    print("\n\n 9. DELETING BUCKET OBJECT :")
    get_bucket('testing-bea').objects.filter(Prefix='temp/').delete()
    list(get_bucket('testing-bea').object_versions.all())
    d1 = delete_bucket_objects('testing-bea', key_prefix='temp/')
    print("\nwith key_prefix: ", d1)
    d2 = delete_bucket_objects('testing-bea')
    print("\nwithout key_prefix: ", d2)
    
    print("\n\n 10. DELETING BUCKET :")
    print('Buckets BEFORE deletion: ')
    list_buckets()
    delete_buckets('testing-bea')
    print('\nBuckets AFTER deletion: ')
    list_buckets()
    
    