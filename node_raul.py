class Node:
    def __init__(self, state, parent = None, operator = None, depth = 0, heuristic = 0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.heuristic = heuristic
        self.depth = depth