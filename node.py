class Node:

    # Similar to this example
    # https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/

    def __init__(self, state, parent = None, depth = 0, heuristic = 0):

        self.state = state

        self.parent = parent

        self.heuristic = heuristic

        self.depth = depth


    # find function in order to find x, y coordinates for euclidian distance

    def find(self, current_state, target):

        for i in range(len(current_state)):

            for j in range(len(current_state[i])):

                if current_state[i][j] == target:

                    return i, j
                
        return None, None


