from app.config import ElasticConfig
from app.awscfg import AWSConfig
from elasticsearch import Elasticsearch, RequestsHttpConnection


def get_es():
    print(es)
    return es


def config_es(app) -> None:
    global es
    awscfg = AWSConfig(ElasticConfig.ES_SERVICE, ElasticConfig.ES_REGION_NAME)
    es = Elasticsearch(
        hosts=[{"host": ElasticConfig.ES_HOST, "port": 443}],
        http_auth=awscfg.auth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
    )


es = None
