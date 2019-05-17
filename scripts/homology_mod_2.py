from itertools import combinations
from tda_utilities.simplicial import Simplex, SimplicialComplex

v0, v1, v2 = Simplex('a'), Simplex('b'), Simplex('c')
e0, e1, e2 = Simplex('a', 'b'), Simplex('a', 'c'), Simplex('b', 'c')

simplicial_circle = SimplicialComplex(v0, v1, v2, e0, e1, e2)

C_0 = [{simplex} for simplex in simplicial_circle.k_chain(0)]
C_1 = [{simplex} for simplex in simplicial_circle.k_chain(1)]

for n in range(2, 4):
    for combo in combinations((v0, v1, v2), n):
        C_0 += [{combo}]

for n in range(2, 4):
    for combo in combinations((e0, e1, e2), n):
        C_1 += [{combo}]
