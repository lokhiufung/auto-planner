from graph import Graph


def main():
    
    # Example use case: project graph for developing a factory for trading strategies

    graph = Graph()

    # Define the goal node
    goal_node = "Develop an efficient process to manufacture profitable trading strategy"

    # Milestone nodes
    node_1 = "Produce the first profitable trading strategy using the process"
    node_2 = "Build a stable automated trading system for deploying strategies"
    node_3 = "Establish a research center for developing new strategies"
    node_4 = "Define the characteristics of a profitable strategy"
    node_5 = "Obtain a robust backtesting framework"
    node_6 = "Create a data pipeline for collecting historical market data"
    node_7 = "Design system architecture for automated trading"
    node_8 = "Implement risk management and position sizing modules"
    node_9 = "Integrate trading system with a broker API"
    node_10 = "Develop a collaborative research workflow"
    node_11 = "Analyze historical trading data to identify patterns"
    node_12 = "Research market inefficiencies for potential opportunities"
    node_13 = "Define metrics for evaluating strategy performance"
    node_14 = "Choose a backtesting framework"
    node_15 = "Deploy the first protfitable trading strategy to live"
    node_16 = "Obtain historical market data"
    node_17 = "Obtain read-for-use historical data"
    node_18 = "Obtain market inefficiencies or patterns with statistical significance"
    node_19 = "Obtain a prototype trading strategy for backtesting"
    node_20 = "Verify the performance of the prototype trading strategy on historical data"
    node_21 = "Demonstrate the viablility of the efficient process to manufacture profitable trading strategy"


    graph.add_node(goal_node, is_goal=True)

    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)
    graph.add_node(node_5)
    graph.add_node(node_6)
    graph.add_node(node_7)
    graph.add_node(node_11)
    graph.add_node(node_12)
    graph.add_node(node_15)
    graph.add_node(node_16)
    graph.add_node(node_17)
    graph.add_node(node_18)
    graph.add_node(node_19)
    graph.add_node(node_20)
    graph.add_node(node_21)


    graph.add_edge(node_21, goal_node)
    graph.add_edge(node_15, node_21)
    graph.add_edge(node_1, node_15)
    graph.add_edge(node_3, node_11)
    graph.add_edge(node_3, node_12)
    graph.add_edge(node_2, node_15)
    graph.add_edge(node_20, node_1)


    # research center
    graph.add_edge(node_17, node_3)
    graph.add_edge(node_4, node_20)
    graph.add_edge(node_5, node_3)
    graph.add_edge(node_11, node_18)
    graph.add_edge(node_12, node_18)
    graph.add_edge(node_18, node_19)
    graph.add_edge(node_19, node_20)
    graph.add_edge(node_6, node_17)
    graph.add_edge(node_16, node_6)

    # automated trading system
    graph.add_edge(node_7, node_2)

    # Save and visualize the graph
    graph.save('project_graph.graphml')
    graph.visualize()


if __name__ == "__main__":
    main()
