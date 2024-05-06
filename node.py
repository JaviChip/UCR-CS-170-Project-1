class Node:

    # Similar to this example
    # https://www.geeksforgeeks.org/8-puzzle-problem-using-branch-and-bound/

    def __init__(self, state, parent = None, depth = 0, heuristic = 0):

        self.state = state

        self.parent = parent

        self.heuristic = heuristic

        self.depth = depth



    # Overides equal comparison function
    def __eq__(self, other):

        return self.state == other.state

    # Used to comapre cost of function with one another

    def __lt__(self, other):

        return (self.heuristic + self.depth) < (other.heuristic + other.depth)


    # find function in order to find x, y coordinates for euclidian distance

    def find(self, current_state, target):

        for i in range(len(current_state)):

            for j in range(len(current_state[i])):

                if current_state[i][j] == target:

                    return i, j
                
        return None, None
    
    def printState(self):
        
        for row in self.state:
            print("  " + "  " + "  " + "  " + " ".join(str(num) for num in row))


