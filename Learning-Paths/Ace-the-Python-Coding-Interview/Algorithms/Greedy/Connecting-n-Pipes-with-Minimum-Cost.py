"""
Time: O(n log n)
Space: O(n)
"""

import heapq

def min_cost(pipes):
    """
    Calculates the minimum cost of connecting pipes
    :param pipes: A list where its length is the number of pipes and indexes are the specific lengths of the pipes.
    :return: The minimum cost
    """

    heapq.heapify(pipes)

    cost = 0

    while len(pipes) > 1:

        first = heapq.heappop(pipes)
        second = heapq.heappop(pipes)

        cost += first + second

        heapq.heappush(pipes, first+second)

    return cost 
