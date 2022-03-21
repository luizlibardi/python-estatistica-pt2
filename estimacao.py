## Estimação
import pandas as pd
import numpy as np
from scipy.stats import norm

dados = pd.read_csv('files/dados.csv')

## Teorema do Limite central

n = 2000
total_de_amostras = 1500

amostras = pd.DataFrame()

# print(amostras)

# for i in range(total_de_amostras):
#     _ = dados.Idade.sample(n)
#     _.index = range(0, len(_))
#     amostras['Amostra_' + str(i)] = _

# print(amostras)

# calculando a distribuição das medias amostrais

amostras.mean().mean()

# Desvio Padrão
amostras.mean().std()
dados.Idade.std()

dados.Idade.std()/ np.sqrt(n)


# Niveis de confiança e Siginificancia

# Erro inferencial

# Intervalos de confiança

media_amostra = 5050
significancia = 0.05
confianca = 1 - significancia
# print( 0.5 + (confianca/ 2))
z = norm.ppf(0.975)


desvio_padrao = 150
n = 20
raiz_de_n = np.sqrt(n)
sigma = desvio_padrao / raiz_de_n


erro = z * sigma

# Calculando Intervalo de Confiança para media

intervalo = (
    media_amostra - erro,
    media_amostra + erro
)

# Calculando com numpy
print(norm.interval(alpha = 0.95, loc = media_amostra, scale = sigma))