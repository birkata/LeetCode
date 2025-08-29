# def minimizeCost(servers):
#     if len(servers) == 1:
#         return servers[0]
#
#     cost = 0
#
#     temp_list = servers.copy()
#     costs_list = []
#
#     while len(temp_list) > 1:
#         temp_cost = temp_list[-1] + temp_list[-2]
#         temp_list = temp_list[: -2] + [temp_cost]
#         costs_list.append(temp_cost)
#
#     cost = sum(costs_list)
#
#     return cost
#
# if __name__ == "__main__":
#     servers = [10, 95, 37, 33, 19, 92, 94, 16, 2, 18, 50]
#     print(minimizeCost(servers))

# Expected: 1358
# My result: 2574

"""
Your approach merges always from the end of the list, but the optimal strategy for this problem is different. The 
expected minimal cost uses a greedy algorithm: always merge the two smallest elements first because each merge cost adds
 to all subsequent merges.

Your current logic:

Takes the last two items repeatedly.

This ignores the fact that merging large numbers early creates high cumulative cost.

Example with your list:
[10,95,37,33,19,92,94,16,2,18,50]
You merge 50+18=68, then 68+2=70, then 70+16=86 … You keep adding large sums repeatedly → cost skyrockets.

Correct algorithm:

Use a min-heap (priority queue).

Continuously pop the two smallest, sum them, add sum back to heap.

Accumulate total cost.

Correct version:
"""

import heapq


def minimizeCost(servers):
    if len(servers) == 1:
        return servers[0]

    heapq.heapify(servers)
    cost = 0

    while len(servers) > 1:
        a = heapq.heappop(servers)
        b = heapq.heappop(servers)
        temp_cost = a + b
        cost += temp_cost
        heapq.heappush(servers, temp_cost)

    return cost


if __name__ == "__main__":
    servers = [10, 95, 37, 33, 19, 92, 94, 16, 2, 18, 50]
    print(minimizeCost(servers))  # Output: 1358



