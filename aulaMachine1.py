import pandas as pd  # Importa a biblioteca pandas, que é usada para manipulação de dados
import numpy as np  # Importa a biblioteca numpy, que é usada para operações numéricas (não é usada aqui, mas pode ser útil)

# Cria um dicionário com chaves e valores que representam dados
data3 = {
    'a': 0.,  # A chave 'a' tem o valor 0.0
    'b': 1.,  # A chave 'b' tem o valor 1.0
    'c': 2.,  # A chave 'c' tem o valor 2.0
    'd': 3.,  # A chave 'd' tem o valor 3.0
}

# Converte o dicionário em uma Série do pandas
s3 = pd.Series(data3)

# Imprime a Série, que terá os índices automaticamente atribuídos (0, 1, 2, 3) para as chaves 'a', 'b', 'c', 'd'
print(s3)
