import math
from node import Node
import heapq as pq
from collections import defaultdict



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
        
    # calculates if a puzzle is unsolvable 
    # In the context of a sliding puzzle, an inversion
    # occurs when a tile precedes another tile with a lower number but is placed after it in the goal state.
        
    def is_solvable(self):

        inversion_count = 0

        flattened_state = sum(self.initialState, [])

        for i in range(len(flattened_state)):

            for j in range(i + 1, len(flattened_state)):

                if flattened_state[i] != 0 and flattened_state[j] != 0 and flattened_state[i] > flattened_state[j]:

                    inversion_count += 1

        return inversion_count % 2 == 0
    
    # Search Algo

    def search(self):

        if not self.is_solvable():

            print("No solution: Puzzle is unsolvable.")

            return False, 0, 0

        initial_node = Node(self.initialState)

        goal_node = Node(self.goalState)

        # Initialize an empty priority queue to store nodes with their respective priorities

        frontier = []

        # Add the initial node to the priority queue with its priority based on heuristic and depth

        pq.heappush(frontier, (initial_node.heuristic + initial_node.depth, initial_node))

        # Keep track of explored nodes to avoid repetition

        explored_set = defaultdict(bool)

        max_queue_size = 1

        # Start the search process

        while True:

            # Check if the frontier is empty, indicating no solution

            if not frontier:

                print("No solution")

                print("Max Queue size: ", max_queue_size)

                print("Explored Nodes: ", len(explored_set))

                return (False, max_queue_size, len(explored_set))

            # Update the maximum queue size

            max_queue_size = max(max_queue_size, len(frontier))

            # Dequeue the node with the lowest priority from the priority queue

            _, curr_node = pq.heappop(frontier)

            # Print the current node's state being expanded

            print("\nThe best state to expand with g(n) =", int(curr_node.depth), "and h(n) =", math.ceil(curr_node.heuristic), "is...")
            curr_node.printState()

            explored_set[tuple(sum(curr_node.state, []))] = True

            # Check if the goal state has been reached
            if curr_node == goal_node:

                print("Solution found at depth", curr_node.depth)

                print("Max queue size:", max_queue_size)

                print("Nodes expanded:", len(explored_set))

                return (True, max_queue_size, len(explored_set))

            else:
                # Expand the current node to generate candidate nodes
                successor_nodes = Problem.expand_node(curr_node)

            
                for node in successor_nodes:
                  
                    state_signature = tuple(sum(node.state, []))

                    if node not in [n[1] for n in frontier] and not explored_set[state_signature]:

                        # Calculate the heuristic value for the candidate node
                        node.heuristic = self.calculate_Heuristic(node)

                        # Add the candidate node to the frontier with its priority
                        pq.heappush(frontier, (node.heuristic + node.depth, node))


        


