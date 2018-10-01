# Created by Minbiao Han and Roman Sharykin
# AI fall 2018

from collections import deque

def search(maze, start, end):

    ### Your code should go here ###

    path = []
    num_nodes_expanded = 0

    stack = deque([("", start)])
    visited = set()
    new_maze = graph(maze)

    while stack:
        path, current = stack.pop()
        if current == end:
            break
        if current in visited:
            continue
        visited.add(current)
        for direction, neighbor in graph[current]:
            stack.append((path + direction, neighbor))

    ### Your search function should return the
    # path for the agent to take,
    # as well as the number of nodes your algorithm searches  ###

    return path, num_nodes_expanded


### feel free to add any aditional support functions for your search here ###
def graph(maze):
    height = len(maze)
    width = len(maze[0]) if height else 0
    graph = {(i, j): [] for j in range(width) for i in range(height) if not maze[i][j]}
    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("S", (row + 1, col)))
            graph[(row + 1, col)].append(("N", (row, col)))
        if col < width and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    return graph