class Node:

    # Similar to this example
    # https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/

    def __init__(self, state, parent = None, depth = 0, heuristic = 0):

        self.state = state

        self.parent = parent

        self.heuristic = heuristic

        self.depth = depth

