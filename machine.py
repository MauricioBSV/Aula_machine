import pandas as pd
import numpy as np

# Dados originais
data2 = np.array(['Maurício', 'Felix', 'Rafael', 'Josemar', 'Jorbeson', 'Carol', 'Caroline', 'Caronine'])
s2 = pd.Series(data2)

# Selecionar apenas os elementos a partir de "Carol"
s2 = s2[s2.isin(['Carol', 'Caroline', 'Caronine'])]

# Resetar o índice
s2.reset_index(drop=True, inplace=True)

print(s2)
