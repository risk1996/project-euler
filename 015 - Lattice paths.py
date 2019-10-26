"""
Solution to
Lattice paths
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""


def find_route_count(x, y):
    routes = [[0 for i in range(x+1)] for j in range(y+1)]
    for j in range(y+1):
        routes[j][0] = 1
    for i in range(x+1):
        routes[0][i] = 1
    for j in range(1, y+1):
        for i in range(1, x+1):
            routes[j][i] = routes[j][i-1] + routes[j-1][i]
    return routes[y][x]


sol = find_route_count(20, 20)
print(sol)
