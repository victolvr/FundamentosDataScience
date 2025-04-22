# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo dos gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("pastel")

# Criando o DataFrame com os dados fornecidos
print("Criando o DataFrame com os dados de vendas...")
data = {
    'Região': ['Norte', 'Norte', 'Sul', 'Sul', 'Norte'],
    'Mês': ['Jan', 'Fev', 'Jan', 'Fev', 'Mar'],
    'Vendas': [1500, np.nan, 2200, 1800, 2000],
    'Despesas': [300, 250, np.nan, 400, 350]
}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)
print("\n")

# Salvando o DataFrame em um arquivo Excel
print("Salvando o DataFrame em um arquivo Excel...")
df.to_excel('vendas.xlsx', index=False)
print("Arquivo 'vendas.xlsx' criado com sucesso!\n")

# 1. Carregando o arquivo e inspecionando os dados
print("1. Carregando o arquivo e inspecionando os dados...")
df_loaded = pd.read_excel('vendas.xlsx')
print("Dados carregados do arquivo:")
print(df_loaded)
print("\nInformações sobre o DataFrame:")
print(df_loaded.info())
print("\nEstatísticas descritivas:")
print(df_loaded.describe())
print("\n")

# 2. Substituindo valores ausentes
print("2. Substituindo valores ausentes...")
# Calculando a mediana da coluna Vendas
vendas_median = df_loaded['Vendas'].median()
print(f"Mediana das Vendas: {vendas_median}")

# Calculando a média da coluna Despesas
despesas_mean = df_loaded['Despesas'].mean()
print(f"Média das Despesas: {despesas_mean}")

# Substituindo os valores ausentes
df_loaded['Vendas'] = df_loaded['Vendas'].fillna(vendas_median)
df_loaded['Despesas'] = df_loaded['Despesas'].fillna(despesas_mean)

print("DataFrame após substituição dos valores ausentes:")
print(df_loaded)
print("\n")

# 3. Agrupando os dados por Região e Mês
print("3. Agrupando os dados por Região e Mês...")
# a. Soma total de vendas
vendas_por_regiao_mes = df_loaded.groupby(['Região', 'Mês'])['Vendas'].sum().reset_index()
print("Soma total de vendas por Região e Mês:")
print(vendas_por_regiao_mes)
print("\n")

# b. Média de despesas
despesas_por_regiao_mes = df_loaded.groupby(['Região', 'Mês'])['Despesas'].mean().reset_index()
print("Média de despesas por Região e Mês:")
print(despesas_por_regiao_mes)
print("\n")

# 4. Combinando horizontalmente as colunas Vendas e Despesas
print("4. Combinando horizontalmente as colunas Vendas e Despesas...")
# Extraindo as colunas como arrays NumPy
vendas_array = df_loaded['Vendas'].values
despesas_array = df_loaded['Despesas'].values

# Combinando horizontalmente (hstack)
combined_array = np.column_stack((vendas_array, despesas_array))
print("Array combinado (Vendas e Despesas):")
print(combined_array)
print("\n")

# 5. Gerando um sumário estatístico
print("5. Gerando um sumário estatístico para todas as colunas numéricas...")
numeric_summary = df_loaded[['Vendas', 'Despesas']].describe()
print(numeric_summary)
print("\n")

# Visualizações adicionais
print("Criando visualizações para melhor compreensão dos dados...")

# Gráfico de barras para vendas por região
plt.figure(figsize=(10, 6))
sns.barplot(x='Região', y='Vendas', data=df_loaded)
plt.title('Vendas por Região')
plt.savefig('vendas_por_regiao.png', dpi=300, bbox_inches='tight')

# Gráfico de barras para despesas por região
plt.figure(figsize=(10, 6))
sns.barplot(x='Região', y='Despesas', data=df_loaded)
plt.title('Despesas por Região')
plt.savefig('despesas_por_regiao.png', dpi=300, bbox_inches='tight')

# Gráfico de dispersão entre Vendas e Despesas
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Vendas', y='Despesas', hue='Região', data=df_loaded, s=100)
plt.title('Relação entre Vendas e Despesas por Região')
plt.savefig('vendas_vs_despesas.png', dpi=300, bbox_inches='tight')

print("Análise concluída! Todos os resultados foram exibidos e os gráficos foram salvos.")
