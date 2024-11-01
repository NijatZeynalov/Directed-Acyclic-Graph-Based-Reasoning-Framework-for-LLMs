# reasoning/dag_constructor.py

import networkx as nx
from typing import Dict, List

class DAGConstructor:
    """
    Constructs a Directed Acyclic Graph (DAG) to represent the reasoning process.
    Nodes represent propositions, critiques, or refinements, with directed edges
    showing logical progression.
    """

    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id: str, node_type: str, content: str):
        """Adds a node to the DAG with the given type (proposition, critique, refinement)."""
        self.graph.add_node(node_id, type=node_type, content=content)

    def add_edge(self, from_node: str, to_node: str):
        """Adds a directed edge between nodes to show reasoning progression."""
        if not nx.has_path(self.graph, to_node, from_node):  # Ensures acyclic nature
            self.graph.add_edge(from_node, to_node)

    def get_dag(self) -> nx.DiGraph:
        """Returns the constructed DAG."""
        return self.graph
