"""Topological Feature Selection Functions"""

class Simplex:
    """Defines a k-simplex object --- vertices can be any object"""
    def __init__(self, *args):
        self.points = tuple(set(args))
        self.dim = len(self.points) - 1 # k-simplex
    
    def __len__(self) -> int:
        return self.dim

    def __getitem__(self, i: int) -> object:
        return self.points[i]

    def __repr__(self):
        return f'{self.k}-simplex: {self.points}'

    def __lt__(self, other):
        return len(self) < len(other)

class SimplicialComplex:
    """Defines a simplicial complex"""
    def __init__(self, simplices):
        self.simplices = list(set(simplices))
        self.simplices.sort()
        self.dim = len(max(self.simplices))

    def __len__(self) -> int:
        return self.dim

    def __getitem__(self, i) -> Simplex:
        return self.simplices[i]

    def __lt__(self, other):
        return len(self) < len(other)

    def chain(self, k):
        """returns the k-chain"""
        raise NotImplementedError

class Chain:
    """Defines a k-Chain"""
    def __init__(self):
        raise NotImplementedError

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

