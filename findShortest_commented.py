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

    # color = [0] + ids
    
    # for i in range(len(graph_from)):
    #     maps[graph_from[i]].append(graph_to[i])
    #     maps[graph_to[i]].append(graph_from[i])

from collections import defaultdict, deque

def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    
    # build adjacency dictionary {from: [to,...,to]}
    adj = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        adj[u].append(v)
        adj[v].append(u)
  
    # initialize deque structure with the pair
    # (current, count) := (val, 0)
    d = deque([(val, 0)])

    # pick the initial color
    start_color = ids[val-1]
    print(f"stc {start_color}")

    # create the set of visited nodes
    visited = set()

    while d: # execute until d is not empty
        print(bool(d))
        print("DEQUE", d)
        current, count = d.popleft()
        print(f"current: {current}, count: {count}")
        print(d)
        visited.add(current)
        print("visited", visited)
        for x in adj[current]:
            print("x selected",x)
            if x not in visited:
                # if node x color is the start color, exit
                # and return count + 1 
                if ids[x-1] == start_color: 
                    print("ECCO", x)
                    return count + 1
                # add x to the visited nodes
                visited.add(x)
                # append the node and increase its count by 1
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
