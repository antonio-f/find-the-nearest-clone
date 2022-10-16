#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#

from collections import defaultdict, deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    adj = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        adj[u].append(v)
        adj[v].append(u)
    d = deque([(val, 0)])
    start_color = ids[val-1]
    visited = set()

    while d: 
        current, count = d.popleft()
        visited.add(current)
        for x in adj[current]:
            if x not in visited:
                if ids[x-1] == start_color: 
                    return count + 1
                visited.add(x)
                d.append((x, count+1))
    return -1   


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    print("answer", ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()