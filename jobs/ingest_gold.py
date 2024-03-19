import pandas as pd

from mongoutil import get_database, to_dataframe, save_to_collection

db_silver = get_database("silver")
db_gold = get_database("gold")

df_emp = to_dataframe(db_silver["empresas"])
df_soc = to_dataframe(db_silver["socios"])

df_emp_soc = pd.merge(df_soc[["cnpj","tipo_socio"]], df_emp[["cnpj","cod_porte"]], how="inner", on=["cnpj"])

group = df_emp_soc.groupby("cnpj").agg(
    flag_socio_extrangeiro=("tipo_socio", lambda x:all((x==3))),
    qtde_socios=("cnpj","count"),
    doc_alvo=("cod_porte",lambda x:((len(x)>1) and all(x==3)))
)

save_to_collection(group.reset_index(),db_silver["fato_socios"])