import boto3

rds_client = boto3.client('rds', region_name='us-west-1')

response = rds_client.describe_orderable_db_instance_options(
    Engine='postgres'
)

for option in response['OrderableDBInstanceOptions']:
    print(option, '>>>>>>>>>>>>>')
    if option['DBInstanceClass'] == 'db.t2.micro':
        print(f"Engine Version: {option['EngineVersion']}, DBInstanceClass: {option['DBInstanceClass']}")