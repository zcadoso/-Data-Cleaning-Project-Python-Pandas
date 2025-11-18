import pandas as pd

def carregar_dados(path):
    return pd.read_csv(path)

def salvar_dados(df, path):
    df.to_csv(path, index=False)
