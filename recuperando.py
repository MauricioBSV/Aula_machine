import pandas as pd  # Importa a biblioteca pandas, que é utilizada para manipulação e análise de dados

# Cria uma Série do pandas com uma lista de valores e índices personalizados
# A lista contém os números de 1 a 5 e os índices são definidos como 'a', 'b', 'c', 'd' e 'e'
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Imprime os valores associados aos índices 'a' e 'b' em uma única linha
# A formatação de string permite incluir múltiplos valores na mesma impressão
s[['a', 'b', 'c', 'd', 'e']]

print(s)