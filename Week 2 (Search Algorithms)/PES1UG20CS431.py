"""
You can create any other helper funtions.
Do not modify the given functions
"""
import queue
import copy


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
    list = []
     
    n = len(cost)                                               
    visited = [0 for i in range(n)]                             
    priority_queue = queue.PriorityQueue()             

    
    priority_queue.put((heuristic[start_point], ([start_point], start_point, 0 , goals)))

   
    while(priority_queue.qsize() != 0):

        
        total_estimated_cost, nodes_tuple = priority_queue.get()
        A_star_path_till_node = nodes_tuple[0]
        node = nodes_tuple[1]
        node_cost = nodes_tuple[2]

       
        if visited[node] == 0:
            visited[node] = 1

            
            if node in goals:
                return A_star_path_till_node

            
            for neighbour_node in range(1, n):
                
                if cost[node][neighbour_node] > 0 and visited[neighbour_node] == 0:

                    
                    total_cost_till_node = node_cost + cost[node][neighbour_node]
                    
                    estimated_total_cost = total_cost_till_node + heuristic[neighbour_node]

                    A_star_path_till_neighbour_node = copy.deepcopy(A_star_path_till_node)
                    A_star_path_till_neighbour_node.append(neighbour_node)
                    priority_queue.put((estimated_total_cost, (A_star_path_till_neighbour_node, neighbour_node, total_cost_till_node)))

    
    

    # TODO
    return list()


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
    
    n = len(cost)                                  
    visited = [0 for i in range(n)]                # Visited Set (0 - not visited, 1 - visited)
    stack = queue.LifoQueue()             
    
    
    stack.put((start_point, [start_point]))

    
    while(stack.qsize() != 0):

        
        node, dfs_path_till_node = stack.get()

    
        if visited[node] == 0:
            visited[node] = 1

            
            if node in goals:
                return dfs_path_till_node

            
            for neighbour_node in range(n-1, 0, -1):
               
                if cost[node][neighbour_node] > 0:
                    
                    if visited[neighbour_node] == 0:
                        
                        dfs_path_till_neighbour_node = copy.deepcopy(dfs_path_till_node)
                        dfs_path_till_neighbour_node.append(neighbour_node)
                        
                        stack.put((neighbour_node, dfs_path_till_neighbour_node))

   
    
    # TODO
    return path()
