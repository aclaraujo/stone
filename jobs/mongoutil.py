import json

import pandas as pd
from pymongo import MongoClient


def get_database(db_name, db_url='mongodb://mongo', db_port=27017):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    client = MongoClient(db_url, db_port,
                         maxPoolSize=50,
                         unicode_decode_error_handler='ignore'
                         )
    return client[db_name]


def save_to_collection(df, coll):
    coll.drop()
    payload = json.loads(df.to_json(orient='records'))
    coll.insert_many(payload)

def to_dataframe(collection):
    df = pd.DataFrame(list(collection.find())).reset_index(drop=True)
    return df