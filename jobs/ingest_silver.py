from mongoutil import get_database

db_bronze = get_database("bronze")

db_silver = get_database("silver")

new_coll_emp = db_silver.get_collection("empresas")

cur_emp = db_bronze['empresas'].aggregate([
  {
    "$replaceRoot": {
      "newRoot": {
        "$arrayToObject": [
          [
            {
              "k": "cnpj","v": "$0"
            },
            {
              "k": "razao_social","v": "$1"
            },
            {
              "k": "natureza_juridica","v": "$2"
            },
            {
              "k": "qualificacao_repsonsavel","v": "$3"
            },
            {
              "k": "capital_social","v": "$4"
            },
            {
              "k": "cod_porte","v": "$5"
            }
          ]
        ]
      }
    }
  }
])

new_coll_emp.drop()
new_coll_emp.insert_many(cur_emp)

cur_soc = db_bronze['socios'].aggregate([
  {
    "$replaceRoot": {
      "newRoot": {
        "$arrayToObject": [
          [
            {
              "k": "cnpj","v": "$0"
            },
            {
              "k": "tipo_socio","v": "$1"
            },
            {
              "k": "nome_socio","v": "$2"
            },
            {
              "k": "documento_socio","v": "$3"
            },
            {
              "k": "codigo_qualificacao_socio","v": "$4"
            }
          ]
        ]
      }
    }
  }
])

new_coll_soc = db_silver.get_collection("socios")

new_coll_soc.drop()
new_coll_soc.insert_many(cur_soc)



