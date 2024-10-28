import numpy as np  # Importa a biblioteca NumPy, que é usada para operações numéricas
import pandas as pd  # Importa a biblioteca pandas, que é utilizada para manipulação e análise de dados
from sklearn.datasets import load_iris  # Importa a função para carregar o conjunto de dados Iris da biblioteca scikit-learn

# Carregar o conjunto de dados Iris, que contém informações sobre diferentes espécies de flores
iris = load_iris()

# Criar um DataFrame a partir dos dados do conjunto Iris
# np.column_stack combina os dados (características) e os alvos (espécies) em uma única estrutura
df_iris = pd.DataFrame(np.column_stack((iris.data, iris.target)), 
                       columns=iris.feature_names + ['target'])  # Define os nomes das colunas usando os nomes das características e adiciona uma coluna para os alvos

# Imprimir o DataFrame, que contém as características das flores e suas respectivas espécies
print(df_iris)
