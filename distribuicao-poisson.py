## Distribuição Poisson

import numpy as np

euler = np.e

# Numero médio de ocorrencias
media = 20

# Numero de Ocorrencias que queremos obter no periodo
k = 25

# Montando a fórmula

probabilidade = ((np.e ** (-media)) * (media ** k)) / (np.math.factorial(k))
print('%0.8f' % probabilidade)

# Utilizando scipy
from scipy.stats import poisson

probabilidade = poisson.pmf(k, media)
print('%0.8f' % probabilidade)
