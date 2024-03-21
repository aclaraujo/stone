#!/usr/bin/env python3

from mongoutil import get_database, insert_many, to_dataframe, to_collection


def main():
    db_bronze = get_database("bronze")
    db_silver = get_database("silver")

    df_emp = to_dataframe(db_bronze["empresas"])

    df_emp.rename({
        "0": "cnpj",
        "1": "razao_social",
        "2": "natureza_juridica",
        "3": "qualificacao_responsavel",
        "4": "capital_social",
        "5": "cod_porte"
    }, inplace=True, axis=1)

    to_collection(db_silver,
                  df_emp[["cnpj", "razao_social", "natureza_juridica", "qualificacao_responsavel", "capital_social",
                          "cod_porte"]],
                  "empresas")

    df_soc = to_dataframe(db_bronze["socios"])
    df_soc.rename({
        "0": "cnpj",
        "1": "tipo_socio",
        "2": "nome_socio",
        "3": "documento_socio",
        "4": "codigo_qualificacao_socio"
    }, inplace=True, axis=1)

    to_collection(db_silver,
                  df_soc[["cnpj", "tipo_socio", "nome_socio", "documento_socio", "codigo_qualificacao_socio"]],
                  "socios")


if __name__ == '__main__':
    main()
