def trace_path(my_dict):  
    routes = []

    for i in my_dict.items():
        routes.append(list(i))
    
    res = []

    visited = {}

    i, j = 0, 0

    while i != len(routes):

        start = routes[i]
        dest = routes[j]

        start1 = str(start)
        dest1 = str(dest)

        if start[-1] == dest[0]:
            if start1 not in visited and dest1 not in visited:
                res.append(start)
                res.append(dest)
                visited[start1] = 1
                visited[dest1] = 1
    
        j += 1


        if j == len(routes):
            i += 1
            j = 0
        
        if i == len(routes) and j == i:
            return res

    return res
