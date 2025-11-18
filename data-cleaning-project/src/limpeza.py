import pandas as pd

# 1. Ler arquivo CSV
df = pd.read_csv("../data/vendas.csv")

print("=== Dataset bruto ===")
print(df)

# 2. Remover linhas completamente vazias
df = df.dropna(how="all")

# 3. Preencher preços faltantes com a média
df["preco"] = df["preco"].fillna(df["preco"].mean())

# 4. Preencher quantidades faltantes
df["quantidade"] = df["quantidade"].fillna(1)

# 5. Preencher loja vazia
df["loja"] = df["loja"].fillna("Loja Não Informada")

# 6. Preencher datas faltantes
df["data"] = df["data"].fillna("2024-01-01")

# 7. Criar coluna de faturamento
df["faturamento"] = df["preco"] * df["quantidade"]

# 8. Gerar relatório por loja
relatorio_lojas = df.groupby("loja")["faturamento"].sum().reset_index()

# 9. Exportar resultados
df.to_csv("../data/vendas_tratadas.csv", index=False)
relatorio_lojas.to_csv("../data/relatorio_lojas.csv", index=False)

print("\n=== Dados tratados ===")
print(df)

print("\n=== Relatório por loja ===")
print(relatorio_lojas)

