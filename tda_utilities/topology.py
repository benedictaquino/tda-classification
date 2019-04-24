"""Topological Feature Selection Functions"""
from itertools import combinations

class Simplex:
    """Defines a k-simplex object"""
    def __init__(self, *points, orientation: int = None):
        """Simplex takes any arguments as points that can make up a k-simplex"""
        self.k = len(set(points)) - 1 # k-simplex
        self.orientation = orientation
        self.points = points
        # recursively initialize arguments as simplices such that each
        # argument passed becomes a 0-simplex
        if self.k == 0: 
            self.faces = None
        else:
            self.faces = tuple( [Simplex(*combo) for combo in combinations(set(points), self.k)])
    
    def __len__(self) -> int:
        return self.k

    def __getitem__(self, i: int) -> object:
        return self.points[i]

    def __repr__(self):
        if self.orientation:
            return f'{self.k}-simplex with orientation {self.orientation}: {" ".join(str(point) for point in self.points)}'
        return f'{self.k}-simplex: {" ".join(str(point) for point in self.points)}'

    def __lt__(self, other) -> bool:
        return len(self) < len(other)

    def orient(self, sigma: int): 
        """assigns an orientation to the simplex"""
        self.orientation = sigma

class SimplicialComplex:
    """Defines a simplicial complex"""
    def __init__(self, simplices):
        # -> set to remove duplicates -> back to list
        self.simplices = list(set(simplices)) 
        self.simplices.sort() # puts lower-dimensional simplices first
        self.k = len(max(self.simplices)) # largest dimension simplex

    def __len__(self) -> int:
        return self.k

    def __getitem__(self, i) -> Simplex:
        return self.simplices[i]

    def __lt__(self, other):
        return len(self) < len(other)

    def __repr__(self, other):
        return f'simplicial {self.k}-complex'

    def chain(self, k):
        """returns the k-chain"""
        raise NotImplementedError

class SimplicialChain:
    """Defines a simplicial k-chain"""
    def __init__(self, complex: SimplicialComplex, orientation: int = 0):
        # TODO: ???
        self.chain = None 
        self.orienation = orientation # this should do something, but what?

    def boundary(self):
        """returns a (k-1)-Chain"""
        raise NotImplementedError

def closure(simplices: set) -> SimplicialComplex:
    """return the closure of the set of simplices"""
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

