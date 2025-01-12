
import networkx as nx

from graph import Graph


def identify_bottlenecks(graph):
    # Calculate betweenness centrality for nodes
    node_centrality = nx.betweenness_centrality(graph, normalized=True)
    # Calculate betweenness centrality for edges
    edge_centrality = nx.edge_betweenness_centrality(graph, normalized=True)

    # Sort nodes and edges by centrality
    sorted_nodes = sorted(node_centrality.items(), key=lambda x: x[1], reverse=True)
    sorted_edges = sorted(edge_centrality.items(), key=lambda x: x[1], reverse=True)

    print("Top Node Bottlenecks (Betweenness Centrality):")
    for node, centrality in sorted_nodes[:5]:
        print(f"Node: {node}, Centrality: {centrality:.4f}")

    print("\nTop Edge Bottlenecks (Betweenness Centrality):")
    for edge, centrality in sorted_edges[:5]:
        print(f"Edge: {edge}, Centrality: {centrality:.4f}")



def main():
    graph = Graph()
    graph.load('project_graph.graphml')
    
    identify_bottlenecks(graph.G)

    
if __name__ == '__main__':
    main()