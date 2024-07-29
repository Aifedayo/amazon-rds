RDS_SECURITY_GROUP_NAME = 'my-rds-public-sg'


class EC2:
    def __init__(self, client):
        self._client = client
        """ :type : pyboto3.ec2 """

    @property
    def create_security_group(self):
        print('I am creating RDS Security Group with name ' + RDS_SECURITY_GROUP_NAME)
        return self._client.create_security_group(
            GroupName=RDS_SECURITY_GROUP_NAME,
            Description='RDS Security Group for Public Access',
            VpcId="vpc-08d64a43de278669e"
        )
