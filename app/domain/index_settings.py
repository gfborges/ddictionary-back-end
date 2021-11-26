settings = {
    "analysis": {
        "analyzer": {
            "default": {
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
        "id": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "title": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "domain": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "group": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "definitions": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "translations": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
        "created_at": {
            "type": "date",
        },
        "image": {
            "type": "text",
            "fields": {"keyword": {"type": "keyword", "ignore_above": 256}},
        },
    }
}
