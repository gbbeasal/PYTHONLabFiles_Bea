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

print("1. CREATE A TOPIC")
def create_sns_topic(topic_name):
    sns = boto3.client('sns')
    sns.create_topic(Name=topic_name)
    return True

def list_sns_topics(next_token=None):
    sns = boto3.client('sns')
    params = {'NextToken': next_token} if next_token else {}
    topics = sns.list_topics(**params)
    return topics.get('Topics', []), topics.get('NextToken', None)

print("\nList of SNS Topics: ", list_sns_topics())
print("\nCreation Status: ", create_sns_topic('price_updates_bea'))
print("\nCreation Status: ", create_sns_topic('price_updates_bea2'))
print("\nList of SNS Topics: ", list_sns_topics())


print("\n\n2. SUBSCRIBE TO A TOPIC")
def list_sns_subscriptions(next_token=None):
    sns = boto3.client('sns')
    params = {'NextToken': next_token} if next_token else {}
    subscriptions = sns.list_subscriptions(**params)
    return subscriptions.get('Subscriptions', []),
    subscriptions.get('NextToken', None)

def subscribe_sns_topic(topic_arn, mobile_number):
    sns = boto3.client('sns')
    params = {
        'TopicArn': topic_arn,
        'Protocol': 'sms',
        'Endpoint': mobile_number,
    }
    res = sns.subscribe(**params)
    print(res)
    return True
    
print("\nList of SNS Subscriptions: ", list_sns_subscriptions())
print("\nSubscription Status: ", subscribe_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates_bea','+639954893030'))
print("\nSubscription Status: ", subscribe_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates_bea','+639176883248'))
print("\nList of SNS Subscriptions: ", list_sns_subscriptions())


print("\n\n3. PUBLISHING A MESSAGE TO A TOPIC")
def send_sns_message(topic_arn, message):
    sns = boto3.client('sns')
    params = {
    'TopicArn': topic_arn,
    'Message': message,
    }
    res = sns.publish(**params)
    print(res)
    return True

print("Send Status :", send_sns_message('arn:aws:sns:ap-southeast-1:337008671328:price_updates_bea', 'Woo Hoodies are no 50% off!'))


print("\n\n4. UNSUBSCRIBING TO A TOPIC")
def unsubscribe_sns_topic(subscription_arn):
    sns = boto3.client('sns')
    params = {
    'SubscriptionArn': subscription_arn,
    }
    res = sns.unsubscribe(**params)
    print(res)
    return True

print("\nList of SNS Subscriptions: ", list_sns_subscriptions())
#delete own number topic subscription
print("\nSubscription Deletion Status: ", unsubscribe_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates_bea:6e600014-c929-44c9-9e60-28bac44a546d'))
print("\nList of SNS Subscriptions: ", list_sns_subscriptions())

print("\n\n5. DELETING A TOPIC")
def delete_sns_topic(topic_arn):
    # This will delete the topic and all it's subscriptions.
    sns = boto3.client('sns')
    sns.delete_topic(TopicArn=topic_arn)
    return True

print("\nList of SNS Topics: ", list_sns_topics())
print("\nDeletion Status: ", delete_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates_bea2'))
print("\nList of SNS Topics: ", list_sns_topics())

