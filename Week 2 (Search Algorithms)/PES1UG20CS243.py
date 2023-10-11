"""
You can create any other helper funtions.
Do not modify the given functions
"""


from importlib.resources import path
import heapq


def A_star_Traversal(cost, heuristic, start_point, goals):
    """
    Perform A* Traversal and find the optimal path 
    Args:
        cost: cost matrix (list of floats/int)
        heuristic: heuristics for A* (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from A*(list of ints)
    """
    path = []
    visited = []
    pqueue = []
    heapq.heappush(pqueue, (heuristic[start_point], [start_point]))
    while(len(pqueue) > 0):
        cur_total_cost, cur_path = heapq.heappop(pqueue)
        cur_node = cur_path[-1]
        cur_total_cost = cur_total_cost - heuristic[cur_node]
        if cur_node in goals:
            path = cur_path
            break
        if cur_node not in visited:
            visited.append(cur_node)
            for i in lex_adj(cur_node, cost):
                if i not in visited:
                    heapq.heappush(
                        pqueue, (cost[cur_node][i] + cur_total_cost + heuristic[i], cur_path+[i]))
    return path


def lex_adj(s, cost):
    """
    Return the costs of traversal from node s in reverse lexical order
    Args:
        s: Node s
        cost: cost matrix
    """
    for i in range(len(cost[s])-1, 0, -1):
        if i != s and cost[s][i] != -1:
            yield i


def DFS_Traversal(cost, start_point, goals):
    """
    Perform DFS Traversal and find the optimal path 
        cost: cost matrix (list of floats/int)
        start_point: Staring node (int)
        goals: Goal states (list of ints)
    Returns:
        path: path to goal state obtained from DFS(list of ints)
    """
    path = []
    path1 = [[start_point]]
    visited = []
    while len(path1) != 0:
        cur_path = path1.pop()
        cur_node = cur_path[-1]
        if cur_node in goals:
            path = cur_path
            break
        if cur_node not in visited:
            visited.append(cur_node)
            for a in lex_adj(cur_node, cost):
                if a not in visited:
                    new_path = cur_path.copy()
                    new_path.append(a)
                    path1.append(new_path)
    return path
