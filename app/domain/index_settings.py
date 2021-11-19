settings = {
    "analysis": {
        "analyzer": {
            "custom_analyzer": {
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "asciifolding",
                    "pt_snowball",
                    "pt_stop",
                ],
            },
        },
        "filter": {
            "pt_snowball": {"type": "snowball", "language": "portuguese"},
            "pt_stop": {"type": "stop", "stopwords": "_brazilian_"},
        },
    }
}

mappings = {
    "properties": {
        "definitions": {
            "title": {"type": "text", "analyzer": "custom_analyzer"},
            "group": {"type": "text", "analyzer": "custom_analyzer"},
            "definitions": {"type": "text", "analyzer": "custom_analyzer"},
            "translations": {"type": "text", "analyzer": "custom_analyzer"},
        }
    }
}
