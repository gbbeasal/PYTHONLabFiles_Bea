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


#LIST LOG GROUPS AND LOG STREAMS
def list_log_groups(group_name=None, region_name=None):
    cwlogs = boto3.client('logs', region_name=region_name)
    params = {
        'logGroupNamePrefix': group_name,
    } if group_name else {}
    res = cwlogs.describe_log_groups(**params)
    return res['logGroups']
    
    
def list_log_group_streams(group_name, stream_name=None, region_name=None):
    cwlogs = boto3.client('logs', region_name=region_name)
    params = {
        'logGroupName': group_name,
    } if group_name else {}
    if stream_name:
        params['logStreamNamePrefix'] = stream_name
    res = cwlogs.describe_log_streams(**params)
    return res['logStreams']

LG = list_log_groups(region_name='ap-southeast-1')
LGS = list_log_group_streams('/aws/lambda/logtest_bea', region_name='ap-southeast-1')
print('\nLog Group Name: ', LG)
print('\nLog Group Streams: ', LGS)

#FILTER LOG EVENTS
def filter_log_events(
    group_name, filter_pat,
    start=None, stop=None,
    region_name=None
    ):
    cwlogs = boto3.client('logs', region_name=region_name)
    params = {
        'logGroupName': group_name,
        'filterPattern': filter_pat,
    }
    if start:
        params['startTime'] = start
    if stop:
        params['endTime'] = stop
    res = cwlogs.filter_log_events(**params)
    return res['events']
    
FLG = filter_log_events('/aws/lambda/logtest_bea', 'INFO Function start', region_name='ap-southeast-1')
print('\nFiltered Logs Events: ', FLG)

from datetime import datetime, timezone
# Must convert to timestamp in milliseconds
start_ts = int(datetime(2020, 2, 18, 16, 46, tzinfo=timezone.utc).timestamp() * 1000)
end_ts = int(datetime(2020, 2, 18, 16, 49, tzinfo=timezone.utc).timestamp() * 1000)

filter_log_events(
    '/aws/lambda/logtest_bea', 'INFO Function start',
    start=start_ts, stop=end_ts,
    region_name='ap-southeast-1'
)