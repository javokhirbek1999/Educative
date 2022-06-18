# v = # of total vertices
# e = # of total edges

# Time:  O(v+e)
# Space: O(v)

def find_mother_vertex(g):
    
    for v in range(g.vertices):
        total_visited = dfs(g, v)
        if total_visited == g.vertices:
            return v
    
    return -1


def dfs(g, s):

    stack = [s]

    visited = [False] * g.vertices
    
    visited[s] = True 
    total_reached = 1

    while stack:

        vert = stack.pop()

        current = g.array[vert].head_node

        while current:
            if not visited[current.data]:
                visited[current.data] = True
                stack.append(current.data)
                total_reached += 1
            current = current.next_element
        
    return total_reached 
