# População e Amostra

# População Finitas

# População Infinitas

## Amostragem Aleatória Simples 
import pandas as pd

dados = pd.read_csv('files/dados.csv')
dados.shape[0]

dados.Renda.mean()

# Seleção de Amostra com Pandas
amostra = dados.sample(n = 100, random_state= 101)
amostra.shape[0]
amostra.Renda.mean()

print(dados.Sexo.value_counts(normalize = True))
print(amostra.Sexo.value_counts(normalize = True))


## Amostragem Estratificada


## Amostragem por Conglomerados


