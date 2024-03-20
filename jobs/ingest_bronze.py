#!/usr/bin/env python3

import logging
import sys

import pandas as pd
from mongoutil import get_database, to_collection

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def mongoimport(csv_path, db, coll_name, cols_names):

    logger.info(f'Loading file {csv_path}')
    df = pd.read_csv(csv_path, header=None, names=cols_names, delimiter=";", encoding="ISO-8859-1", on_bad_lines="skip")
    to_collection(db, df, coll_name)


def main():

    db = get_database("bronze")

    cols_empresas = ["cnpj", "razao_social", "natureza_juridica", "qualificacao_responsavel", "capital_social",
                     "cod_porte", "ente_federativo"]
    mongoimport("files/csv/K3241.K03200Y9.D40210.EMPRECSV", db, "empresas", cols_empresas)

    cols_socios = ["cnpj", "tipo_socio", "nome_socio", "documento_socio", "codigo_qualificacao_socio", "data_sociedade",
                   "codigo_pais", "cpf_rep_legal", "nome_representante", "qualificacao_representante", "faixa_etaria"]
    mongoimport("files/csv/K3241.K03200Y9.D40210.SOCIOCSV", db, "socios", cols_socios)


if __name__ == '__main__':
    main()
