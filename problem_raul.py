from typing import List
from math import sqrt
from node_raul import Node

def print_puzzle(curr_state: List[List[int]]) -> None:
    for row in curr_state:
        for num in row:
            print(num, end=" ")
        print()
    print()

def find_blank_tile(self, curr_state: List[List[int]]) -> List[int]:
        # Create a map to store the coordinates of each number
        num_map = {}
        for i, row in enumerate(curr_state):
            for j, num in enumerate(row):
                num_map[num] = (i, j)
        
        # Get the coordinates of the blank tile (0) and store them in a list
        blank_tile_coords = num_map[0]
        return list(blank_tile_coords)

def h_euclid(self, curr_state: List[List[int]]) -> float:
        h = 0
        goal = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]

        # Create a map to store the coordinates of each number in the goal state
        num_map = {}
        for i, row in enumerate(goal):
            for j, num in enumerate(row):
                num_map[num] = (i, j)

        for i, row in enumerate(curr_state):
            for j, currNum in enumerate(row):
                x2, y2 = num_map[currNum]
                x1, y1 = i, j
                
                euclid = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                h += euclid
        
        # print("H:", h)
        return -1

def is_valid_operator(x, y):
    return 0 <= x < 3 and 0 <= y < 3


class Problem:
    def __init__(self, initialState, goalState = None, heuristic = None):
        self.initialState = initialState
        self.goalState = goalState
        self.heuristic = heuristic

    def solve(self):
        

        initial_h = h_euclid(self.initialState)
        node = Node(None, self.initialState, None, None, 0, initial_h)

        while node.state != self.goalState:
            children = expand(node);

            node = select_next(children);

    def expand(self, node):
        children = []
        
        # Generate child nodes from the current node
        blank_tile_coords = self.find_blank_tile(node.state)
        blank_x, blank_y = blank_tile_coords[0], blank_tile_coords[1]
        
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            new_blank_x, new_blank_y = blank_x + move[0], blank_y + move[1]
            if is_valid_operator(x, y):
                
        

        return children  # Replace pass with your implementation

    def select_next(self, children):
        
        # Choose the next node for expansion
        pass  # Replace pass with your implementation