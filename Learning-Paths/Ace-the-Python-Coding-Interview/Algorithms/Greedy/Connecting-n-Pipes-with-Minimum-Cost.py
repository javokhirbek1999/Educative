"""
Time: O(n log n)
Space: O(1)
"""
def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    total_cost = 0
    current_length = 0

    pipes.sort()

    current_length = pipes[0]+pipes[1]
    total_cost = current_length

    for pipe in pipes[2:]:
        current_length += pipe
        total_cost += current_length
    
    return total_cost
