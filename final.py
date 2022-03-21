from matplotlib import scale
import pandas as pd
import numpy as np
from scipy.stats import norm

dados = pd.read_csv('files/dados.csv')

renda_5000 = dados.query("Renda <= 5000").Renda

sigma = renda_5000.std()

media = renda_5000.mean()

# Calculando o tamanho da amostra

z = norm.ppf(.975)
e = 10
n = (z * (sigma / e)) ** 2
n = int(n.round())
print(n)

# Calculando o intervalo de confiança para a média
 
intervalo = norm.interval(alpha = 0.95, loc = media, scale= (sigma / np.sqrt(n)))
print(intervalo)