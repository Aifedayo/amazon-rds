from client_factory import RDSClient
from rds import RDS


def deploy_resource():
    rds_client = RDSClient().get_client()
    rds = RDS(rds_client)

    rds.create_postgresql_instance()
    print('Creating RDS PostgreSQL instance...')


if __name__ == '__main__':
    deploy_resource()
