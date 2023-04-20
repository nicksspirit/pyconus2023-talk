from itertools import product

import numpy as np
from ortools.graph.python import min_cost_flow

# from ortools.graph.pywrapgraph import SimpleMinCostFlow # if ortools==9.3.10497

# min_cost_flow expects integers and numpy treats infinity as a float
HIGH_COST_VAL = 100

NUM_POWERS = 2
NUM_LOADS = 2
cost_matrix = np.array(
    [[5, 20],
     [HIGH_COST_VAL, 10]]
)

NUM_POWERS = 4
NUM_LOADS = 4
cost_matrix = np.array(
    [[5, 20, 6, HIGH_COST_VAL],
     [6, 34, 6, HIGH_COST_VAL], 
     [HIGH_COST_VAL, 10, 3, 0],
     [7, 8, 2, 0]]
)

print(f"Cost Matrix {cost_matrix.shape}\n", cost_matrix, "\n")

TOTAL_ASSIGNMENTS = NUM_POWERS + NUM_LOADS

start_nodes = [0] * NUM_POWERS
end_nodes = list(range(1, NUM_POWERS + 1))
edge_cost = []

for i, j in product(range(NUM_POWERS), range(NUM_LOADS)):
    cost = cost_matrix[i][j]
    edge_cost.append(cost)

    start_nodes.append(i + 1)
    end_nodes.append(j + NUM_POWERS + 1)

costs = [0] * NUM_POWERS + edge_cost + [0] * NUM_POWERS

start_nodes += list(range(NUM_POWERS + 1, TOTAL_ASSIGNMENTS + 1))
end_nodes += [TOTAL_ASSIGNMENTS + 1] * NUM_LOADS

capacities = [1] * len(start_nodes)
supplies = [NUM_POWERS] + [0] * TOTAL_ASSIGNMENTS + [-NUM_POWERS]

source = 0
sink = TOTAL_ASSIGNMENTS + 1

# Instantiate a SimpleMinCostFlow solver.
smcf = min_cost_flow.SimpleMinCostFlow()

# Add each arc with their respective cost.
for i in range(len(start_nodes)):
    print(start_nodes[i], end_nodes[i], capacities[i], costs[i])
    smcf.add_arc_with_capacity_and_unit_cost(start_nodes[i], end_nodes[i], capacities[i], costs[i])

# Add node supplies.
for i in range(len(supplies)):
    smcf.set_node_supply(i, supplies[i])

# Find the minimum cost flow between node 0 and node 5.
solve_status = smcf.solve()

if solve_status == smcf.OPTIMAL:
    print(f"Total cost = {smcf.optimal_cost()}", "\n")

    for arc in range(smcf.num_arcs()):
        # Can ignore arcs leading out of source or into sink.
        if smcf.tail(arc) != source and smcf.head(arc) != sink:
            # Arcs in the solution have a flow value of 1. Their start and end nodes
            # give an assignment of worker to task.
            if smcf.flow(arc) > 0:
                print(
                    f"Power {smcf.tail(arc)} assigned to Load {smcf.head(arc)}. "
                    f"Cost = {smcf.unit_cost(arc)}"
                )
else:
    print("There was an issue with the min cost flow input.")
    print(f"Status: {solve_status}")
