from tda_utilities.simplicial import (
    Simplex, SimplicialComplex, boundary
)

# 1-simplices
v0 = Simplex(0)
v1 = Simplex(1)
v2 = Simplex(2)
v3 = Simplex(3)

# 2-simplices
e0 = Simplex(0, 1)
e1 = Simplex(0, 2)
e2 = Simplex(0, 3)
e3 = Simplex(1, 2)
e4 = Simplex(1, 3)
e5 = Simplex(2, 3)

# 3-simplices
f0 = Simplex(0, 1, 2)
f1 = Simplex(0, 1, 3)
f2 = Simplex(0, 2, 3)
f2 = Simplex(1, 2, 3)

# 4-simplex
t0 = Simplex(0, 1, 2, 3)

# Simplicial Complexes
triangle = SimplicialComplex(f0)
tetrahedra = SimplicialComplex(t0)

# Boundaries
triangle_boundary = boundary(triangle)
tetrahedra_boundary = boundary(tetrahedra)