import networkx as nx
# from pyvis.network import Network
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_node(self, node, is_goal=False):
        if node in self.G:
            print(f"Node '{node}' already exists.")
        else:
            self.G.add_node(node, is_goal=is_goal)
            print(f"Node '{node}' added.")

    def remove_node(self, node):
        if node in self.G:
            self.G.remove_node(node)
            print(f"Node '{node}' removed.")
        else:
            print(f"Node '{node}' does not exist.")

    def add_edge(self, source_node, target_node):
        if source_node not in self.G or target_node not in self.G:
            print("Both nodes must exist in the graph.")
        elif self.G.has_edge(source_node, target_node):
            print(f"Edge between '{source_node}' and '{target_node}' already exists.")
        else:
            self.G.add_edge(source_node, target_node)
            print(f"Edge added between '{source_node}' and '{target_node}'.")

    def remove_edge(self, source_node, target_node):
        if self.G.has_edge(source_node, target_node):
            self.G.remove_edge(source_node, target_node)
            print(f"Edge between '{source_node}' and '{target_node}' removed.")
        else:
            print(f"Edge between '{source_node}' and '{target_node}' does not exist.")

    def edit_node(self, node, new_node):
        if node not in self.G:
            print(f"Node '{node}' does not exist.")
            return
        if new_node in self.G:
            print(f"Node '{new_node}' already exists.")
        else:
            self.G = nx.relabel_nodes(self.G, {node: new_node})
            print(f"Node '{node}' renamed to '{new_node}'.")

    def save(self, file_path):
        """
        Save the graph to a file in GraphML format.
        :param file_path: Path to the file where the graph will be saved.
        """
        try:
            nx.write_graphml(self.G, file_path)
            print(f"Graph saved to '{file_path}'.")
        except Exception as e:
            print(f"Error saving graph: {e}")

    def load(self, file_path):
        """
        Load a graph from a file in GraphML format.
        :param file_path: Path to the file from which the graph will be loaded.
        """
        try:
            self.G = nx.read_graphml(file_path)
            print(f"Graph loaded from '{file_path}'.")
        except Exception as e:
            print(f"Error loading graph: {e}")


    def visualize(self, file_name="graph.html"):
        """
        Visualize the graph using pyvis.
        :param file_name: The name of the HTML file to generate.
        """
        pos = nx.spring_layout(self.G, seed=42)  # Layout for graph positioning
        # Assign colors: 'red' for goal nodes, 'blue' for regular nodes
        node_colors = [
            'red' if self.G.nodes[node].get('is_goal', False) else 'blue'
            for node in self.G.nodes
        ]

        # Draw the graph
        nx.draw(self.G, pos, with_labels=True, node_color=node_colors, node_size=800)
        plt.show()
        
