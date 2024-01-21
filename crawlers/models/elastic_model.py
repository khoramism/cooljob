from elasticsearch import Elasticsearch
from dotenv import load_dotenv
import os

load_dotenv()

# Access variables
elastic_username = os.getenv('ELASTIC_USERNAME')
elastic_password = os.getenv('ELASTIC_PASSWORD')
print(elastic_username)
es = Elasticsearch("http://localhost:9200", http_auth=(elastic_username, elastic_password)) 

def create_multilingual_index_with_multifields(es, index_name):
    settings = {
        "settings": {
            "analysis": {
                "char_filter": {
                    "zero_width_spaces": {
                        "type": "mapping",
                        "mappings": ["\\u200C=>\\u0020"]
                    }
                },
                "filter": {
                    "persian_stop": {
                        "type": "stop",
                        "stopwords": "_persian_"
                    },
                    "english_stop": {
                        "type": "stop",
                        "stopwords": "_english_"  # You can customize the list of English stopwords
                    }
                },
                "analyzer": {
                    "rebuilt_persian": {
                        "tokenizer": "standard",
                        "char_filter": ["zero_width_spaces"],
                        "filter": [
                            "lowercase",
                            "decimal_digit",
                            "arabic_normalization",
                            "persian_normalization",
                            "persian_stop"
                        ]
                    },
                    "english_analyzer": {
                        "tokenizer": "standard",
                        "filter": ["lowercase", "english_stop"]
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "position": {
                    "type": "text",
                    "analyzer": "rebuilt_persian",
                    "fields": {
                        "english": {
                            "type": "text",
                            "analyzer": "english_analyzer"
                        }
                    }
                },
                "team": {
                    "type": "text",
                    "analyzer": "rebuilt_persian",
                    "fields": {
                        "english": {
                            "type": "text",
                            "analyzer": "english_analyzer"
                        }
                    }
                },
                "city": {
                    "type": "text",
                    "analyzer": "rebuilt_persian",
                    "fields": {
                        "english": {
                            "type": "text",
                            "analyzer": "english_analyzer"
                        }
                    }
                },
                "url": {"type": "keyword"},
                "detail": {
                    "type": "text",
                    "analyzer": "rebuilt_persian",
                    "fields": {
                        "english": {
                            "type": "text",
                            "analyzer": "english_analyzer"
                        }
                    }
                },
                "company": {"type": "keyword"}
            }
        }
    }

    es.indices.create(index=index_name, body=settings)


# create_multilingual_index_with_multifields(
#     es=es, index_name='cool_job'
# )


def insert_data(index_name, job_data):
    es.index(index=index_name, body=job_data)
