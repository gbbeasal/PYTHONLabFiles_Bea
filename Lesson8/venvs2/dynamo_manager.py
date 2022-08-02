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

print("\n\n 1. CREATING A TABLE")
def create_dynamo_table(table_name, pk, pkdef):
    ddb = boto3.resource('dynamodb')
    table = ddb.create_table(
        TableName=table_name,
        KeySchema=pk,
        AttributeDefinitions=pkdef,
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )
    table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    return table
    
table_ko = create_dynamo_table(
'products-bea10',
    pk=[
        {
        'AttributeName': 'category',
        'KeyType': 'HASH',
        },
        {
        'AttributeName': 'sku',
        'KeyType': 'RANGE',
        },
    ],
    pkdef=[
        {
        'AttributeName': 'category',
        'AttributeType': 'S',
        },
        {
        'AttributeName': 'sku',
        'AttributeType': 'S',
        },
    ],
)

print("Created table :", table_ko)


print("\n\n 2. USING AN EXISTING TABLE")
def get_dynamo_table(table_name):
    ddb = boto3.resource('dynamodb')
    return ddb.Table(table_name)

table = get_dynamo_table('products-bea10')
print(f"Table count for existing table: ", table.item_count)

print("\n\n 3. CREATING AN ITEM")
def create_product(category, sku, **item):
    table = get_dynamo_table('products-bea10')
    keys = {
    'category': category,
    'sku': sku,
    }
    item.update(keys)
    table.put_item(Item=item)
    return table.get_item(Key=keys)['Item']

product = create_product(
    'clothing', 'woo-hoodiebea927',
    product_name='Hoodie',
    is_published=True,
    price=Decimal('44.99'),
    in_stock=True
)

product2 = create_product(
    'clothing', 'woo-hoodiebea2927',
    product_name='Hoodie',
    is_published=True,
    price=Decimal('44.99'),
    in_stock=True
)
print("Product 1: ", product)
print("Product 2: ", product2)
print(f"Table count for existing table: ", table.item_count)


print("\n\n 4. UPDATING AN ITEM")
def update_product(category, sku, **item):
    table = get_dynamo_table('products-bea10')
    keys = {
        'category': category,
        'sku': sku,
    }
    expr = ', '.join([f'{k}=:{k}' for k in item.keys()])
    vals = {f':{k}': v for k, v in item.items()}
    table.update_item(
        Key=keys,
        UpdateExpression=f'SET {expr}',
        ExpressionAttributeValues=vals,
    )
    return table.get_item(Key=keys)['Item']

product = update_product('clothing', 'woo-hoodiebea927', in_stock=False,price=Decimal('54.75'))
print("Product 1: ", product)
print("Product 2: ", product2)


print("\n\n 5. DELETING AN ITEM")
def delete_product(category, sku):
    table = get_dynamo_table('products-bea10')
    keys = {
        'category': category,
        'sku': sku,
    }
    res = table.delete_item(Key=keys)
    if res.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
        return True
    else:
        log.error(f'There was an error when deleting the product: {res}')
        return False

resultdel = delete_product('clothing', 'woo-hoodiebea927')
print(resultdel)


print("\n\n 6. BATCH OPERATIONS")
def create_dynamo_items(table_name, items, keys=None):
    table = get_dynamo_table(table_name)
    params = {
        'overwrite_by_pkeys': keys
    } if keys else {}
    with table.batch_writer(**params) as batch:
        for item in items:
            batch.put_item(Item=item)
    return True

items = []
sku_types = ('woo', 'foo')
category = ('apparel', 'clothing', 'jackets')
status = (True, False)
prices = (Decimal('34.75'), Decimal('49.75'), Decimal('54.75'))
for id in range(200):
    id += 1
    items.append({
        'category': random.choice(category),
        'sku': f'{random.choice(sku_types)}-hoodie-{id}',
        'product_name': f'Hoodie {id}',
        'is_published': random.choice(status),
        'price': random.choice(prices),
        'in_stock': random.choice(status),
    })

resultcre = create_dynamo_items('products-bea10', items, keys=['category', 'sku'])
print(resultcre)


print("\n\n 7. SEARCHING ITEMS")
import operator as op
from boto3.dynamodb.conditions import Key, Attr
def query_products(key_expr, filter_expr=None):
    # Query requires that you provide the key filters
    table = get_dynamo_table('products-bea10')
    params = {
        'KeyConditionExpression': key_expr,
    }
    if filter_expr:
        params['FilterExpression'] = filter_expr
    res = table.query(**params)
    return res['Items']

items = query_products(
    Key('category').eq('apparel') & Key('sku').begins_with('woo')
)
len(items)
print("Search Results: ", len(items))


def scan_products(filter_expr):
    # Scan does not require a key filter. It will go through
    # all items in your table and return all matching items.
    # Use with caution!
    table = get_dynamo_table('products-bea10')
    params = {
        'FilterExpression': filter_expr,
    }
    res = table.scan(**params)
    return res['Items']

items = scan_products(
    Attr('in_stock').eq(True)
)
len(items)
print("Scan Results :", len(items))


print("\n\n 8. DELETING A TABLE")
def delete_dynamo_table(table_name):
    table = get_dynamo_table(table_name)
    table.delete()
    table.wait_until_not_exists()
    return True
    
result = delete_dynamo_table('products-bea10')
print(result)
