# Created by Minbiao Han and Roman Sharykin
# AI fall 2018
#http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
#https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2



# node class designed for use with the A-star algorithm
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def search(maze, start, end):

    path = []
    num_nodes_expanded = 0
    maze = mazeToGraph(maze)
    visited = set()
	
    # generate a start and end node according to Node class
    startN = Node(None, start)
    startN.g = 0
    startN.h = 0
    startN.f = 0
    endN = Node(None, end)
    endN.g = 0
    endN.h = 0
    endN.f = 0

    # generate an open and closed list, append start node
    open = []
    closed = []
    open.append(startN)

    # loop until the end node has been reached
    while open:
        # retrieve current node
        currentN = open[0]
        currentIndex = 0
        for index, node in enumerate(open):
            if node.f < currentN.f:
                currentN = node
                currentIndex = index

        # pop current from the open list and add it to the closed list
        open.pop(currentIndex)
        closed.append(currentN)

        # if the end has been reached
        if currentN == endN:
            #print("here2")

            current = currentN
            while current:
                path.append(current.position)
                current = current.parent
            # returns the path in reversed order and number of nodes expanded
            return path[::-1], len(closed)

        # generate adjacent
        adjacent = []
        for nodePosition in maze[currentN.position]:  # adjacent positions (left, right, up, down)
            # generate a new node and append it the list of adjacent
            new_node = Node(currentN, nodePosition)
            adjacent.append(new_node)

        # iterate over adjacent
        for node in adjacent:
			
			#Set adjacent_current_cost?????
            currentCost = currentN.g + 1
            if node in open:
                if node.g <= currentN.g:
                    continue
            elif node in closed:
                if node.g <= currentN.g:
                    closed.remove(node)
                    open.append(node)
                    continue
            else:
                open.append(node)
                node.h = (abs(node.position[0] - endN.position[0])) + (abs(node.position[1] - endN.position[1]))
            node.g = currentCost
            node.parent = currentN
			
def mazeToGraph(maze):
    maze_as_graph = {}  # a dictionary representing the maze
    number_of_rows = len(maze)

    for i in range(number_of_rows):  # for every row in the mze
        some_row = maze[i]
        number_of_columns = len(some_row)
        for j in range(number_of_columns):  # for every position in the row
            if some_row[j] != "%":  # if the position is a legal spot to be in
                maze_as_graph[(i, j)] = []  # make a key for that position whose items will be a list of neighbors

                if maze[i - 1][j] != "%":  # if the position above is also a legal spot to be in
                    maze_as_graph[(i, j)].append((i - 1, j))  # add the position as a neighbor

                if maze[i][j - 1] != "%":  # LEFT
                    maze_as_graph[(i, j)].append((i, j - 1))  # add the position as a neighbor

                if maze[i + 1][j] != "%":  # DOWN
                    maze_as_graph[(i, j)].append((i + 1, j))  # add the position as a neighbor

                if maze[i][j + 1] != "%":  # RIGHT
                    maze_as_graph[(i, j)].append((i, j + 1))  # add the position as a neighbor

    return maze_as_graph  # return the maze as a dictionary