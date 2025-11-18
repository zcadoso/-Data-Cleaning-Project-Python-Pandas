import pandas as pd
from utils import carregar_dados, salvar_dados

def limpar_dados(df):
    df = df.dropna()
    df['total'] = df['quantidade'] * df['preco']
    return df

def main():
    df_raw = carregar_dados("data/raw/vendas_raw.csv")
    df_clean = limpar_dados(df_raw)
    salvar_dados(df_clean, "data/processed/vendas_clean.csv")
    print("Dados processados com sucesso!")

if __name__ == "__main__":
    main()
