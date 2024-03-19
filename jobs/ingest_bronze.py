import pandas as pd
import json

from mongoutil import get_database


def mongoimport(csv_path, db_name, coll_name):

    db = get_database(db_name)
    coll = db[coll_name]
    coll.drop()
    data = pd.read_csv(csv_path, header=None, delimiter=";", encoding="ISO-8859-1")
    json_data = data.to_json(orient='records', force_ascii=False)
    payload = json.loads(json_data)
    coll.insert_many(payload)


mongoimport("files/csv/K3241.K03200Y9.D40210.EMPRECSV", "bronze", "empresas")

mongoimport("files/csv/K3241.K03200Y9.D40210.SOCIOCSV", "bronze", "socios")
