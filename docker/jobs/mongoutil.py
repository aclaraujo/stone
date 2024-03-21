import logging
import sys

import pandas as pd
from pymongo import MongoClient


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def get_database(db_name, db_url='mongodb://mongo', db_port=27017):

    logger.info(f'Trying connect to mongo {db_url}:{db_port}')
    client = MongoClient(db_url, db_port,
                         maxPoolSize=50,
                         unicode_decode_error_handler='ignore'
                         )
    return client[db_name]


def to_collection(db, df, coll_name):

    logger.info(f'Loading docs from collection {coll_name}')
    json_docs = df.to_dict(orient='records')
    logger.info(f'{len(json_docs)} loaded from {coll_name}')
    insert_many(db, coll_name, json_docs)


def to_dataframe(collection):
    logger.info(f'Loading collection')
    df = pd.DataFrame(list(collection.find())).reset_index(drop=True)
    return df


def insert_many(db, coll_name, docs):

    coll = db[coll_name]
    coll.drop()

    docs_to_send = len(list(docs))
    logger.info(f'Send {docs_to_send} documents to collection {coll_name}')
    result = coll.insert_many(list(docs))
    inserted = len(result.inserted_ids)
    logger.info(f'{inserted} Documents inserted in {coll_name}')
