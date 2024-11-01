# visualization/dag_visualizer.py

import matplotlib.pyplot as plt
import networkx as nx


class DAGVisualizer:
    """
    Visualizes the Directed Acyclic Graph (DAG) representing the reasoning process.
    """

    @staticmethod
    def draw_dag(graph: nx.DiGraph):
        """Draws the DAG using Matplotlib."""
        pos = nx.spring_layout(graph)  # positions for all nodes
        nx.draw(graph, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black',
                arrows=True)

        edge_labels = nx.get_edge_attributes(graph, 'content')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

        plt.title("DAG of Reasoning Process")
        plt.show()
