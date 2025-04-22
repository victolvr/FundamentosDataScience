# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando o DataFrame com os dados fornecidos
data = {
    'Região': ['Norte', 'Norte', 'Sul', 'Sul', 'Norte'],
    'Mês': ['Jan', 'Fev', 'Jan', 'Fev', 'Mar'],
    'Vendas': [1500, np.nan, 2200, 1800, 2000],
    'Despesas': [300, 250, np.nan, 400, 350]
}

df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo Excel
df.to_excel('vendas.xlsx', index=False)
print("Arquivo vendas.xlsx criado com sucesso!")

# 1. Carregando o arquivo e inspecionando os dados
df_loaded = pd.read_excel('vendas.xlsx')
print("\nDados carregados do arquivo:")
print(df_loaded)

# 2. Substituindo valores ausentes
# Mediana para Vendas
vendas_median = df_loaded['Vendas'].median()
df_loaded['Vendas'].fillna(vendas_median, inplace=True)

# Média para Despesas
despesas_mean = df_loaded['Despesas'].mean()
df_loaded['Despesas'].fillna(despesas_mean, inplace=True)

print("\nDados após substituição de valores ausentes:")
print(df_loaded)

# 3. Agrupando os dados por Região e Mês
grouped = df_loaded.groupby(['Região', 'Mês']).agg({
    'Vendas': 'sum',
    'Despesas': 'mean'
}).reset_index()

print("\nDados agrupados por Região e Mês:")
print(grouped)

# 4. Combinando horizontalmente as colunas Vendas e Despesas
vendas_despesas = np.column_stack((df_loaded['Vendas'].values, df_loaded['Despesas'].values))
print("\nCombinação horizontal de Vendas e Despesas:")
print(vendas_despesas)

# 5. Gerando sumário estatístico
summary = df_loaded[['Vendas', 'Despesas']].describe()
print("\nSumário estatístico:")
print(summary)

# Salvando os resultados em um novo arquivo
df_loaded.to_excel('vendas_processado.xlsx', index=False)
print("\nArquivo vendas_processado.xlsx criado com sucesso!")
