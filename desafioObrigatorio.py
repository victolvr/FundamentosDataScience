# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurando o estilo dos gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("deep")

# Criando o DataFrame com os dados de vendas
dados_vendas = {
    'Região': ['Norte', 'Norte', 'Sul', 'Sul', 'Norte'],
    'Mês': ['Jan', 'Fev', 'Jan', 'Fev', 'Mar'],
    'Vendas': [1500, np.nan, 2200, 1800, 2000],
    'Despesas': [300, 250, np.nan, 400, 350]
}

# Criando o DataFrame
df_vendas = pd.DataFrame(dados_vendas)

# Salvando o DataFrame em um arquivo Excel
df_vendas.to_excel('vendas.xlsx', index=False)
print("Arquivo 'vendas.xlsx' criado com sucesso!")

# 1. Carregando o arquivo e inspecionando os dados
print("\n1. Carregando e inspecionando os dados:")
df = pd.read_excel('vendas.xlsx')
print(df)

# Verificando informações sobre o DataFrame
print("\nInformações do DataFrame:")
print(df.info())

# Verificando estatísticas descritivas
print("\nEstatísticas descritivas:")
print(df.describe())

# Verificando valores ausentes
print("\nValores ausentes por coluna:")
print(df.isnull().sum())

# 2. Substituindo valores ausentes
print("\n2. Substituindo valores ausentes:")

# Calculando a mediana da coluna 'Vendas'
mediana_vendas = df['Vendas'].median()
print(f"Mediana das Vendas: {mediana_vendas}")

# Calculando a média da coluna 'Despesas'
media_despesas = df['Despesas'].mean()
print(f"Média das Despesas: {media_despesas}")

# Substituindo os valores ausentes
df['Vendas'] = df['Vendas'].fillna(mediana_vendas)
df['Despesas'] = df['Despesas'].fillna(media_despesas)

# Verificando se ainda existem valores ausentes
print("\nValores ausentes após substituição:")
print(df.isnull().sum())

# Exibindo o DataFrame após substituição
print("\nDataFrame após substituição de valores ausentes:")
print(df)

# 3. Agrupando os dados por 'Região' e 'Mês'
print("\n3. Agrupando os dados por 'Região' e 'Mês':")

# Soma total de vendas por região e mês
vendas_por_regiao_mes = df.groupby(['Região', 'Mês'])['Vendas'].sum()
print("\nSoma total de vendas por região e mês:")
print(vendas_por_regiao_mes)

# Média de despesas por região e mês
despesas_por_regiao_mes = df.groupby(['Região', 'Mês'])['Despesas'].mean()
print("\nMédia de despesas por região e mês:")
print(despesas_por_regiao_mes)

# 4. Combinando horizontalmente as colunas 'Vendas' e 'Despesas'
print("\n4. Combinando horizontalmente as colunas 'Vendas' e 'Despesas':")

# Extraindo as colunas como arrays NumPy
vendas_array = df['Vendas'].values
despesas_array = df['Despesas'].values

# Combinando horizontalmente (hstack)
vendas_despesas_hstack = np.column_stack((vendas_array, despesas_array))
print("\nArray combinado (hstack):")
print(vendas_despesas_hstack)

# 5. Gerando sumário estatístico para colunas numéricas
print("\n5. Sumário estatístico para colunas numéricas:")

# Selecionando apenas as colunas numéricas
colunas_numericas = df.select_dtypes(include=[np.number])

# Calculando estatísticas
sumario_estatistico = colunas_numericas.agg(['mean', 'median', 'std'])
print(sumario_estatistico)

# Visualizando os dados
plt.figure(figsize=(12, 8))

# Gráfico de barras para vendas por região
plt.subplot(2, 2, 1)
sns.barplot(x='Região', y='Vendas', data=df)
plt.title('Vendas por Região')

# Gráfico de barras para despesas por região
plt.subplot(2, 2, 2)
sns.barplot(x='Região', y='Despesas', data=df)
plt.title('Despesas por Região')

# Gráfico de dispersão entre vendas e despesas
plt.subplot(2, 2, 3)
sns.scatterplot(x='Vendas', y='Despesas', hue='Região', data=df)
plt.title('Relação entre Vendas e Despesas')

# Boxplot para vendas por região
plt.subplot(2, 2, 4)
sns.boxplot(x='Região', y='Vendas', data=df)
plt.title('Distribuição de Vendas por Região')

plt.tight_layout()
plt.savefig('analise_vendas.png', dpi=300, bbox_inches='tight')
plt.show()

# Salvando o DataFrame processado
df.to_csv('vendas_processado.txt', sep='\t', index=False)
print("\nArquivo 'vendas_processado.txt' criado com sucesso!")
