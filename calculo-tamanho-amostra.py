## Calculo do Tamanho da Amostra

# Variaveis quantitativas e população infinita
import pandas as pd
import numpy as np
from scipy.stats import norm


a = 0.5 + (0.90/2)
z = norm.ppf(a)

sigma = 3323.39
e = 100

n = (z * (sigma / e)) ** 2

int(n.round())

# Exemplo ALura:

media = 45.5
sigma = 15
significancia = 0.10
confianca = 1 - significancia

z = norm.ppf(0.5 + (confianca / 2))
erro_percentual = 0.10
e = media * erro_percentual

n = (z * (sigma / e)) ** 2
n.round()

# Variaveis quantitativas e população Finita

N = 10000
z = norm.ppf((0.5 + (0.95/2)))
s = 12
e = 5

n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
int(n.round())

# Exemplo ALura:
N = 2000
z = norm.ppf((0.5 + (0.95/2)))
s = 0.48
e = 0.3

n = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N-1)))
int(n.round())