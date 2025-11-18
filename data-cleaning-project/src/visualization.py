import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_vendas(path="data/processed/vendas_clean.csv"):
    df = pd.read_csv(path)
    sns.barplot(data=df, x="produto", y="total")
    plt.title("Faturamento por Produto")
    plt.show()
