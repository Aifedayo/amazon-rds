from .client_factory import EC2Client
from .ec2 import EC2

RDS_DB_SUBNET_NAME = 'my-rds-subnet-group'


def create_db_security_group_and_rules():
    ec2_client = EC2Client().get_client()
    ec2 = EC2(ec2_client)

    # Create security group
    security_group = ec2.create_security_group
    # Get id of the sg
    security_group_id = security_group['GroupId']

    print('Created RDS Security group with id ' + security_group_id)

    # Add public access rule to sg
    ec2.add_inbound_rule_to_sg(security_group_id)

    print("Added inbound public access rule to sg with id " + security_group_id)
    return security_group_id


class RDS:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.rds """

    def create_postgresql_instance(self):
        security_group_id = create_db_security_group_and_rules()
        self.create_db_subnet_group()
        print('Creating DB Subnet Group!')
        print("Creating Amazon RDS PostgreSQL DB Instance")
        self._client.create_db_instance(
            DBName="MyPostgreSQLDB",
            DBInstanceIdentifier="mypostgresdb",
            DBInstanceClass='db.t2.micro',
            Engine="postgres",
            EngineVersion='9.6.6',
            Port=5432,
            MasterUsername="postgres",
            MasterUserPassword="mypostgrespassword",
            AllocatedStorage=20,
            MultiAZ=False,
            StorageType="gp2",
            PubliclyAccessible=True,
            VpcSecurityGroupIds=[security_group_id],
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            Tags=[
                {
                    "Key": "Name",
                    "Value": 'Akeem-PostgreSQL-Instance'
                }
            ]
        )

    def create_db_subnet_group(self):
        print('Creating RDS DB Subnet Group ' + RDS_DB_SUBNET_NAME)
        self._client.create_db_subnet_group(
            DBSubnetGroupName=RDS_DB_SUBNET_NAME,
            DBSubnetGroupDescription='My own Subnet group for RDS DB',
            SubnetIds=[
                'subnet-0f684f9f3626fed2f',
                'subnet-0c3297816a0f02c6b',
                'subnet-018eb4d73923bb4aa'
            ]
        )
