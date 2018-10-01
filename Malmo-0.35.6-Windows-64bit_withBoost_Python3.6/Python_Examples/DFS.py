# Created by Minbiao Han and Roman Sharykin
# AI fall 2018

def search(maze, start, end):
	path = []
	num_nodes_expanded = 0

	new_maze = mazeToGraph(maze)  # convert the text maze into a graph
	stack = [[start]]
	visited = set()

	while stack:
		path = stack.pop()
		current_position = path[-1]
		
		if current_position == end:  # once the goal has been deque'd, terminate the algorithm
			break

		if current_position not in visited:

			for adjacent in new_maze[current_position]:
				newPath = list(path)
				newPath.append(adjacent)
				stack.append(newPath)
				num_nodes_expanded += 1
			visited.add(current_position)

	return path, num_nodes_expanded


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