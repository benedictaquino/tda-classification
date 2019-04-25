"""Topological Feature Selection Functions"""
from __future__ import annotations
from itertools import combinations


class Simplex:
    """Defines a k-simplex object"""
    def __init__(self, *points, orientation: int = None):
        """Simplex takes arguments as points that can make up a k-simplex"""
        self.k = len(set(points)) - 1  # k-simplex
        self.orientation = orientation
        self.points = tuple(set(points))

    def __len__(self) -> int:
        return self.k

    def __getitem__(self, i: int) -> object:
        return self.points[i]

    def __repr__(self):
        return f'{self.k}-simplex: '\
            + ' '.join(str(point) for point in self.points)

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def __eq__(self, other) -> bool:
        if type(other) == self.__class__:
            return set(self.points) == set(other.points)
        return False

    def __hash__(self) -> int:
        return hash(self.points)

    def faces(self, index: int = None) -> tuple:
        if not self:
            return None
        return tuple([Simplex(*combo)
                      for combo in combinations(set(self.points), self.k)])

    def orient(self, sigma: int):
        """assigns an orientation to the simplex"""
        self.orientation = sigma


class SimplicialComplex:
    """Defines a simplicial complex"""
    def __init__(self, simplices: list):
        # -> set to remove duplicates -> back to list
        self.simplices = list(simplices)
        self._build_complex()
        self.simplices.sort()  # puts lower-dimensional simplices first
        self.k = len(max(self.simplices))  # largest dimension simplex

    def _build_complex(self):
        """add all faces of each simplex"""
        for simplex in self.simplices:
            if simplex:
                for face in simplex.faces():
                    if face not in self.simplices:
                        self.simplices.append(face)

    def __len__(self) -> int:
        return self.k

    def __getitem__(self, i) -> Simplex:
        return self.simplices[i]

    def __lt__(self, other):
        return len(self) < len(other)

    def __repr__(self):
        return f'simplicial {self.k}-complex'

    def closure(self, simplices: list) -> SimplicialComplex:
        """return the closure of the subset of simplices in a k-complex"""
        try:
            return closure(self, simplices)
        except AttributeError:
            raise TypeError('Pass in list of objects with type Simplex')

    def chain(self, k):
        """returns the k-chain"""
        raise NotImplementedError


def closure(k_complex: SimplicialComplex,
            simplices: list) -> SimplicialComplex:
    """return the closure of the subset of simplices in a k-complex"""
    for simplex in simplices:
        if simplex:
            for face in simplex.faces():
                if face not in simplices:
                    simplices.append(face)
    return SimplicialComplex(simplices)


class SimplicialChain:
    """Defines a simplicial k-chain"""
    def __init__(self, complex: SimplicialComplex, orientation: int = 0):
        # TODO: ???
        self.chain = None
        self.orienation = orientation

    def boundary(self):
        """returns a (k-1)-Chain"""
        raise NotImplementedError


def star(simplices: set) -> SimplicialComplex:
    """return the star of the set of simplices"""
    raise NotImplementedError


def link(simplices: set) -> SimplicialComplex:
    """return the link of the set of simplices"""
    raise NotImplementedError


class Filtration:
    """Filtration object
    """
    # TODO: All of this I guess
    def __init__(self):
        raise NotImplementedError

    def create_filtration(self):
        raise NotImplementedError
