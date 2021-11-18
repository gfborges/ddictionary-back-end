import boto3
from app.config import ElasticConfig
from requests_aws4auth import AWS4Auth


class AWSConfig:
    def __init__(self, service: str, region_name: str) -> None:
        self.__client = boto3.Session(
            aws_access_key_id=ElasticConfig.ES_ACCESS_KEY,
            aws_secret_access_key=ElasticConfig.ES_SECRET_KEY,
            region_name=region_name,
        )
        creds = self.__client.get_credentials()
        self.__creds = creds
        self.__auth = AWS4Auth(
            creds.access_key,
            creds.secret_key,
            region_name,
            service,
            session_token=self.__creds.token,
        )

    @property
    def auth(self):
        return self.__auth
