#!/usr/bin/env python3

import logging
import sys

import pandas as pd

from mongoutil import get_database, to_dataframe, to_collection

logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)


def main():
    db_silver = get_database("silver")
    db_gold = get_database("gold")

    df_emp = to_dataframe(db_silver["empresas"])
    df_soc = to_dataframe(db_silver["socios"])

    logger.info(f'Merging collections')
    df_emp_soc = pd.merge(df_soc[["cnpj", "tipo_socio"]], df_emp[["cnpj", "cod_porte"]], how="inner", on=["cnpj"])

    logger.info(f'Grouping socios data')
    group = df_emp_soc.groupby("cnpj").agg(
        flag_socio_extrangeiro=("tipo_socio", lambda x: all((x == 3))),
        qtde_socios=("cnpj", "count"),
        doc_alvo=("cod_porte", lambda x: ((len(x) > 1) and all(x == 3)))
    )

    to_collection(db_gold, group.reset_index(), "fato_socios")


if __name__ == '__main__':
    main()
