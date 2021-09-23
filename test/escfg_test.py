from pytest_elasticsearch import factories

es_my_proc = factories.elasticsearch_proc(port=None)
es_test = factories.elasticsearch("elasticsearch_my_proc")


def config_es_test():
    return


def get_es():
    return es_test
