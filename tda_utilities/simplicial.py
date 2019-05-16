"""Topological Feature Selection"""
from __future__ import annotations
from itertools import combinations, product
from collections import Counter
from typing import Generator


class Simplex(frozenset):
    """Defines a k-simplex object"""
    __slots__ = []

    def __new__(cls, *points):
        """Simplex takes arguments as points that can make up a k-simplex"""
        return super().__new__(cls, points) if points else frozenset()

    @property
    def points(self) -> frozenset:
        """points of the simplex"""
        return list(self)

    @property
    def k(self) -> int:
        """dimension of the simplex"""
        return len(self) - 1

    @property
    def boundary(self) -> KChain:
        """the union of faces of the simplex"""
        if self.k:
            combos = combinations(self, self.k)
            return KChain(Simplex(*combo) for combo in combos)
        return set()

    @property
    def interior(self) -> set:
        """the complement of the boundary"""
        interior = set()
        for k in range(1, self.k):
            combos = combinations(self, k)
            interior |= {Simplex(*combo) for combo in combos}
        return interior

    def __repr__(self):
        return f'{self.k}-simplex: {self.points}'

    def __lt__(self, other):
        if type(other) is Simplex:
            if self.k < other.k:
                return self.k < other.k
            elif self.k == other.k:
                return self.points < other.points
        else:
            return super().__lt__(other)


class SimplicialComplex(set):
    """Defines a simplicial complex"""
    def __init__(self, *simplices):
        """adds all faces of simplices passed in to simplicial complex"""
        super().__init__(simplices)
        for simplex in set(simplices):
            self |= simplex.boundary | simplex.interior

        self.__points = {pt for simplex in simplices for pt in simplex}
        self.__k = max(simplices).k
        self.__k_counter = Counter([simplex.k for simplex in self])

        euler_number = self.k_counter[0]
        for k in range(1, self.k + 1):
            if k % 2 == 0:
                euler_number += self.k_counter[k]
            else:
                euler_number -= self.k_counter[k]

        self.__euler_number = euler_number

    @property
    def simplices(self) -> set:
        """simplices in the complex"""
        return set(self)

    @property
    def points(self) -> set:
        """the points in the complex"""
        return self.__points

    @property
    def k(self) -> int:
        """dimension of the complex"""
        return self.__k

    @property
    def k_counter(self) -> Counter:
        """Counter holding the counts of the number of k-simplices"""
        return self.__k_counter

    @property
    def euler_number(self) -> int:
        """the Euler number of the complex"""
        return self.__euler_number

    def __repr__(self) -> str:
        return f'simplicial {self.k}-complex'

    def closure(self, *simplices) -> SimplicialComplex:
        """return the closure of the subset of simplices in a k-complex"""
        if type(simplices[0]) is SimplicialComplex:
            if not simplices[0].issubset(self):
                raise ValueError('not a subset of the complex')
            return simplices[0]
        elif type(simplices[0]) is set:
            simplex_set = simplices[0]
        else:
            simplex_set = set(simplices)
        if not simplex_set.issubset(self):
            raise ValueError('not a subset of the complex')
        return SimplicialComplex(*simplex_set)

    def star(self, *simplices) -> SimplicialComplex:
        """return the star of the set of simplices"""
        star = set()
        if type(simplices[0]) is SimplicialComplex:
            simplex_set = simplices[0].simplices
        else:
            simplex_set = set(simplices)
        for simplex_1, simplex_2 in product(simplex_set, self):
            if simplex_1 in self.closure(simplex_2):
                star.add(simplex_2)
        return star if star else None

    def link(self, *simplices) -> SimplicialComplex:
        """return the link of the set of simplices"""
        if type(simplices[0]) is SimplicialComplex:
            simplex_set = simplices[0].simplices
        else:
            simplex_set = set(simplices)
        star = self.star(*simplex_set)
        closed_star = self.closure(*star)
        return closed_star - star

    def _k_simplices(self, k: int) -> Generator[Simplex, None, None]:
        """returns a generator of k-simplices in the complex"""
        return (simplex for simplex in self if simplex.k == k)

    def k_chain(self, k: int) -> set:
        """returns the set of k-simplices in the complex"""
        return KChain(self._k_simplices(k))

    def boundary(self, k: int = None) -> KChain:
        """returns the boundary of the k-simplices in the complex"""
        if k is None:
            return KChain(face for simplex in self._k_simplices(self.k)
                          for face in simplex.boundary)
        elif k > self.k:
            raise ValueError(f'no {k}-simplices in the complex')
        elif k <= 0:
            raise ValueError('k must be greater than 0')
        return KChain(face for simplex in self._k_simplices(k)
                      for face in simplex.boundary)


class KChain(set):
    """defines a boundary of a k-simplex or a simplicial k-complex"""
    __slots__ = ['_KChain__boundary', '_KChain__k']

    def __init__(self, simplices):
        self.__boundary = 0  # boundary of boundary is 0
        super().__init__(simplices)
        self.__k = max(self).k

    @property
    def boundary(self) -> int:
        """the boundary of a boundary"""
        return self.__boundary

    @property
    def k(self) -> int:
        """the dimension of the chain"""
        return self.__k

    def __add__(self, other) -> KChain:
        """modulo 2"""
        if type(other) is not KChain:
            raise TypeError('k-chain can only be added to another k-chain')
        elif self.k == other.k:
            kchain_sum = Counter(self) + Counter(other)
            mod_2 = {sx for sx, cnt in kchain_sum.items() if cnt % 2}
        else:
            raise ValueError('cannot add k-chains of different dimensions')
        return KChain(mod_2) if mod_2 else 0


def boundary(entity, *args, **kwargs) -> KChain:
    """defines the boundary operator"""
    bdry = getattr(entity, 'boundary')
    if callable(bdry):
        return bdry(*args, **kwargs)
    return bdry
