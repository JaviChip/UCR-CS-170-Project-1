from node import Node
import copy


class Problem:

    @staticmethod

    def move_up(current_state, i, j):

        if i > 0:

            new_state = [row[:] for row in current_state]  # Deep copy of the puzzle state

            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]  # Swap tiles

            return new_state
        
        else:

            return None
        


    @staticmethod

    def move_down(current_state, i, j):

        if i + 1 < len(current_state):

            new_state = [row[:] for row in current_state]  # Deep copy of the puzzle state

            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]  # Swap tiles

            return new_state
        
        else:

            return None
        
    @staticmethod 

    def move_left(current_state, i, j):

        if j > 0:

            new_state = [row[:] for row in current_state]  # Deep copy of the puzzle state

            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]  # Swap tiles

            return new_state
        
        else:

            return None

    @staticmethod

    def move_right(current_state, i, j):

        if j + 1 < len(current_state[0]):

            new_state = [row[:] for row in current_state]  # Deep copy of the puzzle state

            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]  # Swap tiles

            return new_state
        
        else:

            return None
        
    @staticmethod

    def expand_node (node):

        successor_nodes = []

        i, j = node.find(node.state, 0)
        
        # Define move functions
        move_functions = [

            ("up", Problem.move_up),
            ("down", Problem.move_down),
            ("left", Problem.move_left),
            ("right", Problem.move_right)
        ]
        
        for direction, move_func in move_functions:

            new_state = move_func(node.state, i, j)

            if new_state is not None and new_state != node.state:
                
                successor_nodes.append(Node(new_state, node, node.depth + 1, node.heuristic))

        return successor_nodes


    
    def __init__(self, initialState, goalState = None, heuristic = None):

        self.initialState = initialState

        self.goalState = goalState
        
        self.heuristic = heuristic


    # Calculates misplaced tile heurisitic value h(n)  

    def misplaced(self, node):

        count = 0

        for i in range(len(node.state)):

            for j in range(len(node.state[i])):

                if node.state[i][j] != 0 and node.state[i][j] != self.goalState[i][j]:

                    count += 1

        return count
    
    # calculates euclidean distance value h(n) 
    
    def euclidean(self, node):
        distance = 0
        state_size = len(node.state)  # Assuming the puzzle is square, so len(node.state) represents both rows and columns
        target_state = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        for i in range(state_size):

            for j in range(state_size):

                currNum = node.state[i][j]

                # Ignore the empty cell (0)
                if currNum == 0:
                    continue

                # Calculate the expected position (goal state) of the current number
                expected_row = (currNum - 1) // state_size

                expected_col = (currNum - 1) % state_size

                # Calculate the Euclidean distance between the current and expected positions
                row_sqrdDiff = (i - expected_row) ** 2
                col_sqrdDiff = (j - expected_col) ** 2

                euclidean_distance = (row_sqrdDiff + col_sqrdDiff) ** 0.5

                # Add the Euclidean distance to the total distance
                distance += euclidean_distance

        return distance
    
    def calculate_Heuristic(self, node: Node):

        # 1 => Uniform Cost Search == 0
        # 2 => Missing Tile Heuristic 
        # 3 => Eucledian Distance Heursitic

        if self.heuristic == 1:

            return 0
        
        elif self.heuristic == 2:

            return self.misplaced(node)
        
        elif self.heuristic == 3:

            return self.euclidean(node)
        
        else:

            return 0


