# Topological Feature Selection Functions

class SimplicialComplex:
    """Simplicial Complex object containing list of vertices, edges, faces,
    and tetrahedra
    """
    # TODO: Optimize/vectorize methods with numpy
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []
        self.tetrahedra = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_face(self, face):
        self.faces.append(face)

    def add_tetrahedron(self, tetrahedron):
        self.tetrahedra.append(tetrahedra)

    def add_vertices(self, vertices):
        for vertex in vertices:
            self.add_vertex(vertex)

    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def add_faces(self, faces):
        for face in faces:
            self.add_face(face)

    def add_tetrahedra(self, tetrahedra):
        for tetrahedron in tetrahedra:
            self.add_tetrahedron(tetrahedra)

class Filtration:
    """Filtration object
    """
    # TODO: All of this I guess
    def __init__(self):
        self.complex_list = []

    def create_filtration(self):
        pass

