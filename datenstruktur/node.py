import datenstruktur.interfaces as interfaces


class Node(interfaces.Node):
    """See interfaces.Node class."""

    def __init__(self, label) -> None:
        self.label = label
        self._edges = set()
        self.neighbours = []
        self._info = None
        self._degree = 0
        self._in_degree = 0
        self._out_degree = 0

    def __str__(self) -> str:
        return str(self.label)

    def __hash__(self) -> int:
        return hash(self.label)

    @property
    def info(self):
        """See interfaces.Node class."""
        return self._info

    @info.setter
    def info(self, val):
        """See interfaces.Node class."""
        self._info = val

    @property
    def degree(self):
        """See interfaces.Node class."""
        return self._degree

    @property
    def in_degree(self):
        """See interfaces.Node class."""
        return self._in_degree

    @property
    def out_degree(self):
        return self._out_degree

    @property
    def visited(self):
        """See interfaces.Node class."""
        return self._visited

    @visited.setter
    def visited(self, val):
        """See interfaces.Node class."""
        self._visited = val

    def get_neighbours(self):
        """See interfaces.Node class."""
        return self.neighbours

    def has_edge(self, to_node):
        """See interfaces.Node class."""
        return to_node in self.neighbours
