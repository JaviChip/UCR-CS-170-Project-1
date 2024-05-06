from typing import List
from math import sqrt
from node_raul import Node

class Problem:
    def __init__(self, initialState, goalState=None, heuristic=None):
        self.initialState = initialState
        self.goalState = goalState
        self.heuristic = heuristic

    def solve(self):

        node = Node(self.initialState, None, None, 0, 0)

        while node.state != self.goalState:
            children = self.expand(node)
            node = self.select_next(children)

            # print("Current State:")
            # self.print_puzzle(node.state)
            print("d:", node.depth)
            print("h:", node.heuristic)
            print("Selected State:")
            self.print_puzzle(node.state)

    def expand(self, node):
        children = []

        # make sure to only check nodes that haven't been checked before

        # Generate child nodes from the current node
        blank_tile_coords = self.find_blank_tile(node.state)
        blank_x, blank_y = blank_tile_coords[0], blank_tile_coords[1]

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            new_blank_x, new_blank_y = blank_x + move[0], blank_y + move[1]
            if self.is_valid_operator(new_blank_x, new_blank_y):
                # Create a new state by swapping the positions of the blank tile and the tile in the direction of the move
                new_state = [row[:] for row in node.state]  # Create a copy of the current state
                new_state[blank_x][blank_y], new_state[new_blank_x][new_blank_y] = new_state[new_blank_x][new_blank_y], new_state[blank_x][blank_y]
                # Calculate the heuristic value for the new state
                new_h = self.h_euclid(new_state)
                # Create a new child node with the updated state, parent node, and other attributes
                new_node = Node(new_state, None, None, node.depth + 1, new_h)
                # Add the new child node to the list of children
                children.append(new_node)

                # Print the puzzle for the new child
                # print("Child State:")
                # self.print_puzzle(new_state)

        return children

    def select_next(self, children):
        # Choose the next node for expansion based on the smallest f(n) value
        min_f = float('inf')
        selected_node = None

        for child in children:
            f = child.depth + child.heuristic
            # print("d:", child.depth)
            # print("h:", child.heuristic)
            # print("F:", f)
            if f < min_f:
                min_f = f
                selected_node = child

        return selected_node

    def print_puzzle(self, curr_state: List[List[int]]) -> None:
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
        return h

    def is_valid_operator(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3
