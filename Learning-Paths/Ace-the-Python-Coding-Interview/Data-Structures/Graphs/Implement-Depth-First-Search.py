def dfs_traversal(g, source):
    result = ""

    stack = [source]
    visited = {}
    while stack:

        vert = stack.pop()
        result += str(vert)

        current = g.array[vert].head_node

        while current:
            if current.data not in visited:
                stack.append(current.data)
                visited[current.data] = 1
                current = current.next_element
    return result
