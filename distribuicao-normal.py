# Distribuição Normal

import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [], 
        index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
        columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada

media = 1.7
desvio_padrao = 0.1
z = (1.8 - media) / desvio_padrao

z = (1.9 - media) / desvio_padrao
probabilidade = 1 - 0.9767
probabilidade = 1 - norm.cdf(-z) # com scipy

print(probabilidade)

probabilidade = 0.8413
# print(f'Probabilidade de {probabilidade}')

# Consultando tabela normal com Python
z = (85 - 70) / 5
# print(norm.cdf(z))

# Valores especificos 
probabilidade = (0.8413 - 0.5) * 2
# print(probabilidade)

# Utilizando scipy
# probabilidade = norm.cdf(z_superior) - norm.cdf(z_inferior)
# print(probabilidade)

media = 300
desvio_padrao = 50
z = (350 - media) / desvio_padrao
probabilidade = norm.cdf(z) - (1 - norm.cdf(z))
# print(probabilidade)

