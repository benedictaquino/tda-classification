"""Topological Feature Selection Functions"""

class Simplex:
    """Defines a k-simplex object --- vertices can be any object"""
    def __init__(self, *args):
        self.k = len(args) - 1 # k-simplex
        self.points = args
    
    def __len__(self) -> int:
        return self.k

    def __getitem__(self, i: int) -> object:
        return self.points[i]

    def __repr__(self):
        return f'{self.k}-simplex: {self.points}'

class SimplicialComplex:
    """Defines a simplicial complex"""
    # TODO: all of this
    def __init__(self):
        pass
    # I want to calculate simplicial k-chains, boundaries, cycles, etc. from
    # this class --- not sure yet if they should be methods or functions

def closure(S: set) -> SimplicialComplex:
    """return the closure of the complex"""
    pass

def star(S: set) -> SimplicialComplex:
    """return the star of the complex"""
    pass

def link(S: set) -> SimplicialComplex:
    """return the link of the complex"""
    pass

class Filtration:
    """Filtration object
    """
    # TODO: All of this I guess
    def __init__(self):
        self.complex_list = []

    def create_filtration(self):
        pass

