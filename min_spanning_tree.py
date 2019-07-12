import itertools

node_set=[1, 2, 3, 4, 5, 6, 7, 8, 9]
edge_set=set([(1, 2), (1, 4), (2, 3), (2, 4), (2, 9), (3, 4), (3, 5), (3, 9), (4, 5), (5, 6), (5, 7), (5, 9), (6, 7), (6, 8), (7, 8), (7, 9), (8, 9)])
cost={(1, 2): 3,
      (1, 4): 6,
      (2, 3): 2,
      (2, 4): 4,
      (2, 9): 9,
      (3, 4): 2,
      (3, 5): 9,
      (3, 9): 8,
      (4, 5): 9,
      (5, 6): 4,
      (5, 7): 5,
      (5, 9): 7,
      (6, 7): 1,
      (6, 8): 4,
      (7, 8): 3,
      (7, 9): 9,
      (8, 9): 10}

from gurobipy import *
min_span_tree=Model("Minimum Spanning Tree")
x=min_span_tree.addVars(edge_set, vtype=GRB.BINARY)

min_span_tree.setObjective(sum(cost[i]*x[i] for i in edge_set), GRB.MINIMIZE)

min_span_tree.addConstr(sum(x[i] for i in edge_set)==len(node_set)-1, "Spanning tree")

subtour_range=range(3, len(node_set)+1)

for i in subtour_range:
    subsets=set(itertools.combinations(node_set, i))
    for j in subsets:
        possible_edges=set(itertools.combinations(j, 2))
        existing_edges=set.intersection(possible_edges, edge_set)
        if len(existing_edges) > 0:
            min_span_tree.addConstr(sum(x[k] for k in existing_edges)<=i-1, "subtour elimination[%d][%d][%d] %i%k%j")

min_span_tree.optimize()
x_disp=min_span_tree.getAttr('x', x)
print(x_disp)
