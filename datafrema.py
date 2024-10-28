import pandas as pd  # Importa a biblioteca pandas, que é utilizada para manipulação e análise de dados

# Cria uma lista chamada 'data' com valores inteiros de 1 a 5
data = [1, 2, 3, 4, 5]

# Converte a lista em um DataFrame do pandas
# Um DataFrame é uma estrutura de dados bidimensional, semelhante a uma tabela, onde as colunas podem ter diferentes tipos de dados
df = pd.DataFrame(data)

# Imprime o DataFrame resultante
# Por padrão, o DataFrame terá um índice numérico (0, 1, 2, ...) e uma única coluna, que contém os valores da lista
print(df)
