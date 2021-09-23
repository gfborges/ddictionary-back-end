import boto3
from app.config import ElasticConfig
from requests_aws4auth import AWS4Auth


class AWSConfig:
    def __init__(self, service: str, region_name: str) -> None:
        self.__client = boto3.Session(
            aws_access_key_id=ElasticConfig.ACCESS_KEY,
            aws_secret_access_key=ElasticConfig.SECRET_KEY,
            region_name=region_name,
        )
        self.__creds = self.__client.get_credentials()
        self.__auth = AWS4Auth(
            self.__creds.access_key,
            self.__creds.secret_key,
            region_name,
            service,
            session_token=self.__creds.token,
        )

    @property
    def auth(self):
        return self.__auth
