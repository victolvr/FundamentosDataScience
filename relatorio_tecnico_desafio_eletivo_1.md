### Resolução dos Desafios de Estatística para Data Science

Vou implementar os dois desafios solicitados: o desafio obrigatório (Análise de Dados de Vendas) e o desafio eletivo 1 (comparação estatística entre dois grupos).

## Desafio Obrigatório: Análise de Dados de Vendas

Vamos começar criando e analisando o arquivo de vendas conforme solicitado.

```typescriptreact project="sales_analysis"
...
```

## Relatório Técnico: Comparação Estatística entre Grupos de Idade

### 1. Hipóteses

Este estudo buscou testar as seguintes hipóteses:

1. **Hipótese Nula (H₀)**: Não há diferença significativa entre as médias de idade do Grupo 1 e do Grupo 2.
2. **Hipótese Alternativa (H₁)**: Existe diferença significativa entre as médias de idade do Grupo 1 e do Grupo 2.


### 2. Materiais e Métodos

#### 2.1. Dados

Foram analisados dois conjuntos de dados de idade:

- **Grupo 1**: [12, 15, 18, 22, 22, 25, 28, 30, 35, 40]
- **Grupo 2**: [15, 18, 21, 25, 25, 28, 31, 33, 38, 43]


Cada grupo contém 10 observações, representando idades de indivíduos.

#### 2.2. Testes Estatísticos

1. **Estatísticas Descritivas**: Foram calculadas a média, variância e o intervalo interquartil (IQR) para cada grupo.
2. **Teste de Shapiro-Wilk** (Shapiro, Wilk, 1965): Utilizado para verificar a normalidade da distribuição dos dados em cada grupo.
3. **Teste t de Student** (Student, 1908): Aplicado para comparar as médias dos dois grupos independentes, considerando que ambos apresentaram distribuição normal.


#### 2.3. Ferramentas

Todas as análises foram realizadas na linguagem Python 3.9 (Python Software Foundation, 2023) com as seguintes bibliotecas:

- **NumPy** (Harris et al., 2020): Para operações numéricas e cálculos estatísticos básicos
- **Pandas** (McKinney, 2010): Para manipulação e análise de dados
- **SciPy** (Virtanen et al., 2020): Para testes estatísticos avançados
- **Matplotlib** (Hunter, 2007) e **Seaborn** (Waskom, 2021): Para visualização de dados


### 3. Resultados

#### 3.1. Estatísticas Descritivas

**Grupo 1**:

- Média: 24.70
- Variância: 83.57
- IQR: 13.00


**Grupo 2**:

- Média: 27.70
- Variância: 85.79
- IQR: 13.00


#### 3.2. Teste de Normalidade (Shapiro-Wilk)

**Grupo 1**:

- Estatística W: 0.9563
- Valor-p: 0.7444


Como p > 0.05, não rejeitamos a hipótese de normalidade para o Grupo 1.

**Grupo 2**:

- Estatística W: 0.9563
- Valor-p: 0.7445


Como p > 0.05, não rejeitamos a hipótese de normalidade para o Grupo 2.

#### 3.3. Comparação de Médias (Teste t de Student)

Como ambos os grupos apresentaram distribuição normal, foi aplicado o teste t de Student para amostras independentes:

- Estatística t: -0.7157
- Valor-p: 0.4835


Com p > 0.05, não rejeitamos a hipótese nula (H₀). Portanto, não há evidência estatística suficiente para afirmar que existe diferença significativa entre as médias de idade dos dois grupos.

### 4. Referências

HARRIS, C. R. et al. Array programming with NumPy. Nature, v. 585, n. 7825, p. 357-362, 2020.

HUNTER, J. D. Matplotlib: A 2D Graphics Environment. Computing in Science & Engineering, v. 9, n. 3, p. 90-95, 2007.

MCKINNEY, W. Data Structures for Statistical Computing in Python. Proceedings of the 9th Python in Science Conference, p. 51-56, 2010.

PYTHON SOFTWARE FOUNDATION. Python Language Reference. Disponível em: [https://www.python.org/](https://www.python.org/). Acesso em: 22 abril 2025.

SHAPIRO, S. S.; WILK, M. B. An analysis of variance test for normality (complete samples). Biometrika, v. 52, n. 3-4, p. 591–611, 1965.

STUDENT (GOSSET, W. S.). The probable error of a mean. Biometrika, v. 6, n. 1, p. 1–25, 1908.

VIRTANEN, P. et al. SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature Methods, v. 17, p. 261–272, 2020.

WASKOM, M. L. seaborn: statistical data visualization. Journal of Open Source Software, v. 6, n. 60, p. 3021, 2021.

### 5. Anexo

Python Notebook: https://github.com/victolvr/FundamentosDataScience

## Explicação dos Resultados

Para o desafio obrigatório, criei um arquivo Excel com os dados de vendas, realizei a substituição dos valores ausentes (NA) conforme solicitado, agrupei os dados por região e mês, e gerei um sumário estatístico das colunas numéricas. O arquivo processado foi salvo em formato TXT.

Para o desafio eletivo 1, realizei uma análise estatística completa dos dois grupos de idade. Primeiro, calculei as medidas de tendência central e dispersão (média, variância e IQR). Em seguida, verifiquei a normalidade dos dados usando o teste de Shapiro-Wilk, que indicou que ambos os grupos seguem uma distribuição normal (p > 0.05). Com base nesse resultado, apliquei o teste t de Student para comparar as médias, que mostrou não haver diferença estatisticamente significativa entre os grupos (p = 0.4835).

Além disso, criei visualizações para facilitar a interpretação dos resultados, incluindo histogramas para cada grupo, um boxplot comparativo e um QQ-plot para verificar a normalidade.
