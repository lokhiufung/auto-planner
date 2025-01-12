import networkx as nx

from graph import Graph


def main():
    graph = Graph()
    graph.load('project_graph.graphml')

    # Find the critical path in the graph (assumes the graph is a DAG)
    critical_path = nx.dag_longest_path(graph.G)
    print("\nCritical Path:")
    print(" -> ".join(critical_path))


if __name__ == '__main__':
    main()