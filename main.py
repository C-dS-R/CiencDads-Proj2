# %%
import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# %%
def leitura_csvs(csv_names: dict ,pasta_csvs="dataset"):
    """Lê os CSVs do dataset Olist 2016-2018

    Retorna um dicionário de DataFrames."""
    dfs = {}  #dicionario onde serão guardados os dataframes
    #preenche o dicionario dos DFs, (usando as mesmas chaves)
    for key_name in csv_names.keys():
        dfs[key_name] = pd.read_csv(os.path.join(pasta_csvs, csv_names[key_name]))
    #retorno
    return dfs

# %%
#CSVs
csvs = {
  "orders": "olist_orders_dataset.csv",
  "items": "olist_order_items_dataset.csv",
  "payments": "olist_order_payments_dataset.csv",
  "reviews": "olist_order_reviews_dataset.csv",
  "customers": "olist_customers_dataset.csv",
  "geo": "olist_geolocation_dataset.csv",
  "products": "olist_products_dataset.csv",
  "sellers": "olist_sellers_dataset.csv",
  "translations": "product_category_name_translation.csv"
}

# %%
dataframes = leitura_csvs(csvs)
print(dataframes['orders'].columns)
