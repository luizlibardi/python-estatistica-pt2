## Distribuição de Probabilidade

#### ==== Distribuição Binominal ==== ####
# Possibilidade de ocorrencia de duas categorias, que somadas, formam um espaço amostral

from scipy.special import comb
from scipy.stats import binom

# combinacoes = comb(25, 20)
# print(combinacoes)

# probabilidade = 1/combinacoes

# print('%0.15f' % probabilidade)

n = 10

numero_de_alternativas_por_questao = 3

p = 1 / numero_de_alternativas_por_questao

q = 1 - p

k = 5

(comb(n, k) * (p ** k) * (q ** (n-k))) # Montando a estrutura da formula

binom.pmf(k, n, p) # Forma reduzida

binom.pmf(5, n, p) + binom.pmf(6, n, p) + binom.pmf(7, n, p) + binom.pmf(8, n, p) + binom.pmf(9, n, p) + binom.pmf(10, n, p)

binom.pmf([5, 6, 7, 8, 9, 10], n , p).sum()

1 - binom.cdf(4, n , p)

probabilidade  = binom.sf(4, n, p)

print('%0.8f' % probabilidade)