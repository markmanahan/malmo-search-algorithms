# Created by Minbiao Han and Roman Sharykin
# AI fall 2018



def search(maze, start, end):

    ### Your code should go here ###

    path = []
    num_nodes_expanded = 0

    stack = [start]

    while stack:
        current = stack.pop()

        if current == end:
            break

        if current in path:
            continue

        path.append(current)
        num_nodes_expanded += 1

        if maze[current[0] - 1][current[1]] != "%":
            stack.append((current[0] - 1, current[1]))

        if maze[current[0] + 1][current[1]] != "%":
            stack.append((current[0] + 1, current[1]))

        if maze[current[0]][current[1] + 1] != "%":
            stack.append((current[0], current[1] + 1))

        if maze[current[0]][current[1] - 1] != "%":
            stack.append((current[0], current[1] - 1))

    ### Your search function should return the
    # path for the agent to take,
    # as well as the number of nodes your algorithm searches  ###

    return path, num_nodes_expanded


### feel free to add any aditional support functions for your search here ###