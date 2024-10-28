import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import numpy as np  # Importa a biblioteca NumPy para operações numéricas (não usada diretamente aqui, mas pode ser útil)

# Cria um dicionário com chaves e valores que representam dados
data4 = {
    'a': 0.,  # A chave 'a' tem o valor 0.0
    'b': 1.,  # A chave 'b' tem o valor 1.0
    'c': 2.,  # A chave 'c' tem o valor 2.0
    'd': 3.,  # A chave 'd' tem o valor 3.0
}

# Converte o dicionário em uma Série do pandas, especificando uma ordem diferente para os índices
s4 = pd.Series(data4, index=['b', 'c', 'd', 'a'])  # Os índices são definidos na ordem: 'b', 'c', 'd', 'a'

# Imprime a Série, que mostra os valores associados aos índices especificados
print(s4)
