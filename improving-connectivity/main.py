from io import StringIO
import pandas as pd
import networkx as nx
import numpy as np

import matplotlib.pyplot as plt

freight_activity = """
pickup,delivery,cost
A,B,13
A,C,14
A,D,10
A,E,10
A,G,16
B,C,12
C,A,14
E,F,30
E,G,23
G,A,16
"""

graph_df = pd.read_csv(StringIO(freight_activity))

graph: nx.DiGraph = nx.from_pandas_edgelist(
    df=graph_df,
    source="pickup",
    target="delivery",
    edge_attr=["cost"],
    create_using=nx.DiGraph,
)

nx.draw(graph, with_labels=True)
plt.show()

print("Identified Leaf nodes")
for node in graph.nodes:
    if graph.out_degree(node) == 0:
        print(f"Leaf Node: {node}")


def calc_beta_index(network: nx.DiGraph) -> float:
    e = len(network.edges())
    v = len(network.nodes())

    return np.round(e / v, 2)


def calc_alpha_index(network: nx.DiGraph) -> float:
    e = len(network.edges())
    v = len(network.nodes())

    denom_part_a = (v * (v - 1)) / 2
    denom_part_b = v - 1

    return np.round((e - v) / (denom_part_a - denom_part_b), 2)


print("\nCurrent alpha and beta index")
print(f"Beta Index: {calc_beta_index(graph)}")
print(f"Alpha Index: {calc_alpha_index(graph)}")

print("\nRemove edges pointing to leaf node.")
graph.remove_edges_from([("A", "D"), ("E", "F")])
graph.remove_nodes_from(["D", "F"])

nx.draw(graph, with_labels=True)
plt.show()

print(f"Beta Index: {calc_beta_index(graph)}")
print(f"Alpha Index: {calc_alpha_index(graph)}")
