"""Topological Feature Selection Functions"""
from __future__ import annotations
from itertools import combinations, product
from collections import Counter

NONETYPE_ERROR_MESSAGES = (
    "unsupported operand type(s) for -: 'NoneType' and 'set'",
    "unsupported operand type(s) for |=: 'set' and 'NoneType'",
    "unsupported operand type(s) for |: 'NoneType' and 'NoneType'",
    "'NoneType' object is not iterable"
)


class Simplex:
    """Defines a k-simplex object"""
    def __init__(self, *points):
        """Simplex takes arguments as points that can make up a k-simplex"""
        self.__points = frozenset(points)
        self.__k = len(self.points) - 1
        if self:
            combos = combinations(self.points, self.k)
            self.__boundary = {Simplex(*combo) for combo in combos}
            self.__interior = set()
            for k in range(1, self.k):
                combos = combinations(self.points, k)
                self.__interior |= {Simplex(*combo) for combo in combos}
        else:
            self.__boundary = None
            self.__interior = None

    @property
    def points(self) -> frozenset:
        """points of the simplex"""
        return self.__points

    @property
    def k(self) -> int:
        """dimension of the simplex"""
        return self.__k

    @property
    def boundary(self) -> set:
        """the union of faces of the simplex"""
        return self.__boundary

    @property
    def interior(self) -> set:
        """the complement of the boundary"""
        return self.__interior

    def __len__(self) -> int:
        return self.k

    def __contains__(self, other) -> object:
        return other in self.points

    def __repr__(self):
        point_string = ' '.join(str(point) for point in self.points)
        return f'{self.k}-simplex: ' + point_string

    def __eq__(self, other) -> bool:
        if type(other) == self.__class__:
            return self.points == other.points
        return False

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __hash__(self) -> int:
        return hash(self.points)


class SimplicialComplex:
    """Defines a simplicial complex"""
    def __init__(self, *simplices):
        """adds all faces of simplices passed in to simplicial complex"""
        simplex_set = set(simplices)
        for simplex in simplices:
            try:
                simplex_set |= simplex.boundary | simplex.interior
            except TypeError as error_message:
                if str(error_message) in NONETYPE_ERROR_MESSAGES:
                    pass
                else:
                    raise TypeError(error_message)

        self.__simplices = simplex_set
        self.__points = {pt for simplex in simplices for pt in simplex.points}
        self.__k = len(max(simplices))
        self.__k_counter = Counter([simplex.k for simplex in self.simplices])

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
        return self.__simplices

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

    def __len__(self) -> int:
        return len(self.simplices)

    def __repr__(self) -> str:
        return f'simplicial {self.k}-complex'

    def __iter__(self) -> iter:
        return self.simplices.__iter__()

    def __contains__(self, other) -> bool:
        return other in self.simplices

    def __eq__(self, other) -> bool:
        return self.simplices == other.simplices

    def closure(self, *simplices) -> SimplicialComplex:
        """return the closure of the subset of simplices in a k-complex"""
        if not set(simplices).issubset(self.simplices):
            raise ValueError('not a subset of the complex')
        return SimplicialComplex(*simplices)

    def star(self, *simplices) -> SimplicialComplex:
        """return the star of the set of simplices"""
        simplex_set = set(simplices)
        star = set()
        for simplex_1, simplex_2 in product(simplex_set, self.simplices):
            if simplex_1 in self.closure(simplex_2):
                star.add(simplex_2)
        return star if star else None

    def link(self, *simplices) -> SimplicialComplex:
        """return the link of the set of simplices"""
        simplex_set = set(simplices)
        star = self.star(*simplex_set)
        closed_star = self.closure(*star).simplices
        return closed_star - star

    def issubcomplex(self, other: SimplicialComplex) -> bool:
        """checks if the complex is a subcomplex of another complex"""
        return self.simplices <= other.simplices

    def k_simplices(self, k: int) -> set:
        """returns the set of k-simplices in the complex"""
        return {simplex for simplex in self.simplices if simplex.k == k}

    def boundary(self, k: int) -> set:
        """returns the boundary of the k-simplices in the complex"""
        if k > self.k:
            raise ValueError(f'no {k}-simplices in the complex')
        elif k <= 0:
            raise ValueError('k must be greater than 0')
        return {face for sx in self.k_simplices(k) for face in sx.boundary}
