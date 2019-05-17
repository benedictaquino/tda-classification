"""defines classes and functions for simplicial homology modulo 2"""
from __future__ import annotations
from collections import Counter


class Chain(set):
    """defines a boundary of a k-simplex or a simplicial k-complex"""
    __slots__ = ['_Chain__boundary', '_Chain__k']

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

    def __add__(self, other) -> Chain:
        """modulo 2"""
        if type(other) is not Chain:
            raise TypeError('k-chain can only be added to another k-chain')
        elif self.k == other.k:
            kchain_sum = Counter(self) + Counter(other)
            mod_2 = {sx for sx, cnt in kchain_sum.items() if cnt % 2}
        else:
            raise ValueError('cannot add k-chains of different dimensions')
        return Chain(mod_2) if mod_2 else 0


def boundary(entity, *args, **kwargs) -> Chain:
    """defines the boundary operator"""
    bdry = getattr(entity, 'boundary', None)
    if callable(bdry):
        return bdry(*args, **kwargs)
    return bdry
