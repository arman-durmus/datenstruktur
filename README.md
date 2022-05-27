# Datenstruktur

The Datenstruktur group intends to provide to the other groups the graph data structures necessary for implementing their own algorithms (<em>self-explaining</em>). This includes Edge, Node, Graph classes in different variations like un/directed, un/weighted or bipartite, and also their respective interfaces.

---

## Weekly Reports
<details>
<summary>Week 01 (21.04.-27.04.)</summary>

* Recherche über Struktur und Arten von Graphen sowie Verwendungsmöglichkeiten
* Erkundung der Möglichkeiten und möglicher Problemstellen durch testweise Implementierung
* darunter: Strukturen (Graph, Knoten, Kante, Adjazenzmatrix) mit Funktionalität und Algorithmen (Breitensuche)
* Besprechung des weiteren Vorgehens und erste Aufgabenteilung
</details>

<details>
<summary>Week 02 (28.04.-04.05.)</summary>

* Wir haben einige rudimentäre Interfaces für Graphs, Edges und Nodes implementiert.
* Die in der Vorlesung besprochenen Methoden haben wir als abstrakte Methoden entworfen und beginnen einige davon als konkrete Klassen zu implementieren.
* Für Methoden wie add_edge, add_node (usw) haben wir einfache grundlegende Implementationen geschrieben.
* Für gerichtete und ungerichtete Graphen haben wir schonmal einen einfachen Test Case erstellt.
* Wir haben begonnen uns Überlegungen zu bipartiten Graphen und deren Funktionsweise gemacht, sowie einige Entwurfsentscheidungen getroffen wie z.B. Signaturen bzw. Rückgabewerte bestimmter Methoden und Hierarchien von Interfaces/Klassen.

- In dieser Woche haben wir einige Grundlagen gelegt auf denen wir in den kommenden Wochen aufbauen wollen. Wir finden uns in das Thema ein und haben die interne Kommunikation erarbeitet.
</details>

<details>
<summary>Week 03 (05.05.-11.05.)</summary>

* Anpassung des Codes, um Style Guides zu entsprechen (PEP 8 - Style Guide for Python Code, Google Python Style Guide für Docstrings) -> Blank Lines, Docstrings, snake_case, …
* Docstrings für Klassen und Methoden (lückenhaft), ausstehend noch für Module
* Vollständige Implementierung der Interfaces und Einführung der poetry
Weiterführende Implementierung der Klasse Node, Graph und Edge. (An den Klassen gibt es noch Optimierungsbedarf, aber die Funktionalität steht im Vordergrund)
* Testing für Bipartite Graphen
* Topological Sorting
* Strukturierung unserer Kommunikation durch das Ampeln nützlicher Links und das Umstrukturieren der internen Kommunikation
</details>

<details>
<summary>Week 04 (12.05.-18.05.)</summary>

Woche 4 (12.5.-18.5.)
* Priorisierung von Unit Tests. (An Funktionalität haben wir den anderen Gruppen vorerst genug zur Verfügung gestellt. Dort ist zeitliche Luft; weitere Funktionalität ruhig nach Bedarf.) Mit den Unit Tests können wir auf ein sauberes Fundament bauen. Neben der Fehlerbehebung hätten die anderen Gruppen dann auch Beispielcode.
* Einbringung der Code-Formatierer black und isort.
* Pre-commit hooks für die Code-Formatierer prüfen Formatierung des Codes, bevor der Commit durchgeht. Problem: Muss von jedem manuell mit poetry run pre-commit install installiert werden.
* Weiterführende Implementierungen, u. A.
    * Weitere Unit Tests
    * Topological Sorting
    * Umwandlung Node.neighbors property zu Methode
    * Abkürzungen bfs, dfs für breadth_first_search() und depth_first_search(), Entfernen von Prints bei Rückgabe von Listen
    * Ergänzung fehlender konkreter Graph-Klassen (vorerst als Platzhalter)
    * create_graph() zur Erstellung des benötigten Graphen anhand von boolschen Argumenten für weighted, directed und bipartite.
    * Fehlerbehebungen
    * Edge.get_endpoints() gibt nun ein frozenset-Objekt zurück
    * Verbesserung der __hash__()-Methoden entsprechend der Empfehlung der [Python3 Dokumentation](https://docs.python.org/3/reference/datamodel.html?highlight=__hash__#object.__hash__)
    * add_node() mit Node-Objekt als Eingabe implementiert.
    * add_edge() mit Edge-Objekt als Eingabe implementiert, wobei es eine neue Edge-Objekt zurückgibt.
    * detect_circle() für ungerichtete Graphen implementiert, mit Positiv- und Negativ- Test
* Unit Tests sinnvoll separiert und in neues Unterverzeichnis verschoben
* Umbenennung von Variablen und Methoden und Dateien für bessere Verständlichkeit und Löschen von redundantem Code.
* Anpassung imports dahingehend, dass alle anderen Gruppen aus unserem Repository importieren können.
* Sortierung der Reihenfolge der Klassen und Methoden.
* Ausbau der README.md
</details>

---

## View Documentation
Use [pydoc](https://docs.python.org/3/library/pydoc.html) to make use of the source code documentation. <br>
View the documentation in a browser with
>`python3.10 -m pydoc -b`

---

## Followed Style Guides
### <u>[PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)</u> (<em>primarily</em>)
<s>Especially... <br>
> [Blank Lines](https://peps.python.org/pep-0008/#blank-lines)<br>
> [Imports](https://peps.python.org/pep-0008/#imports)<br>
</s>

**Update:** We now let the formatting be done through the code formatter [<em>black</em>](https://pypi.org/project/black/):

>`pip3 install black` \
>`black {source_file_or_directory}` # Format source_file or directory. \
>`black graph.py` # (e.g.) Format the graph.py file.

Since <em>black</em> doesn't format imports as needed, we further use [<em>isort</em>](https://pypi.org/project/isort/):

>`pip3 install isort` \
>`isort {source_file_or_directory}` # Format source_file or directory. \
>`isort ../datenstruktur` # (e.g.) Format all files in directory from inside datenstruktur/.

**Attention!** Neither <em>black</em> nor <em>isort</em> do format the docstrings. This we need keep doing by hand.

**Update 2:** A pre-commit hook was set up so <em>black</em> and <em>isort</em> run before a commit passes.

### <u>[Google Python Style Guide for Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)</u>
Especially pay attention to this quote:<br>
>`"Be sure to use the right style for module, function, method docstrings and inline comments."`

---

## Code Examples
This section might be filled if time permits. Meanwhile we suggest looking into the [unit tests](https://git.imp.fu-berlin.de/swp-algorithmen-22/datenstruktur/-/tree/main/datenstruktur/unit_tests) (which also have yet to be sorted out, and will).

**Update:** Below, a small sample of graph functionality.
```python
from datenstruktur.graph import Graph, create_graph
from datenstruktur.node import Node
from datenstruktur.edge import Edge

################
# Create graph.
g = create_graph(weighted=False, directed=False, bipartite=False)

# Create a node and add it to the graph.
A = Node("A")
g.add_node(A)

# Create a node with the graph's method, which returns a node.
B = g.add_node("B")
C = g.add_node(Node("C"))

# Add a list (any iterable) of nodes. This returns a list.
D, E, F = g.add_nodes(["D", "E", "F"])
GHI = g.add_nodes(["G", "H", "I"]) # type(GHI) -> <class 'list'>

####################################
# Again with a dictionary for nodes, this time as directed graph.
g = create_graph(False, True, False)
nodes = dict()
new = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

nodes.update(zip(new, g.add_nodes(new)))

# Remove a node from graph.
g.remove_node(nodes["I"])
del nodes["I"]

# Time to create edges.
g.add_edges(
    [
        (nodes["A"], nodes["B"]),
        (nodes["B"], nodes["C"])
    ]
)

# Does this graph contain a cycle?
has_cycle = g.detect_cycle() # False

g.add_edge(nodes["C"], nodes["A"])
has_cycle = g.detect_cycle() # True

# Let's test DFS and BFS.
g.add_edges(
    [
        (nodes["B"], nodes["H"]),
        (nodes["C"], nodes["D"]),
        (nodes["C"], nodes["G"]),
        (nodes["D"], nodes["E"]),
        (nodes["D"], nodes["F"]),
        (nodes["E"], nodes["F"]),
        (nodes["F"], nodes["G"])
    ]
)

print("BFS traversal: ", end="")
[print(n, end="") for n in g.bfs(nodes["A"])] # g.bfs = g.breadth_first_search
print("\nDFS traversal: ", end="")
[print(n, end="") for n in g.dfs(nodes["A"])] # g.dfs = g.depth_first_search

g.remove_edge(nodes["C"], nodes["A"])
print("\nDFS traversal: ", end="")
[print(n, end="") for n in g.dfs(nodes["A"])] # g.dfs = g.depth_first_search

print("\nTopological sorting: ", end="")
[print(n, end="") for n in g.toposort()] # g.toposort = g.topological_sort

# Get source and destination node of edge.
edge = g.edges.pop()
src_node, dest_node = edge.get_endpoints()
print("\nGet endpoints of random edge:", src_node, dest_node)

# We want the neighbors of a node in the graph.
print("\nGet node neighbors of D: ", end="")
[print(n, end="") for n in g.get_node_neighbours(nodes["D"])]
print()
```
---

## Currently working on...
**11.05.22:** It will take a couple of weeks to have a consistent structure, codebase and documentation.

## Authors
Arman Durmus, Lorenzo Melchior, Stefan Schuck, Tarik Basakkiran  