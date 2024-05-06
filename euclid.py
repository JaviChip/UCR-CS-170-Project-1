from typing import List
from math import sqrt

def print_puzzle(curr_state: List[List[int]]) -> None:
    for row in curr_state:
        for num in row:
            print(num, end=" ")
        print()
    print()

class Problem:
    def __init__(self, puzzle: List[List[int]], solverithm: int) -> None:
        self.puzzle = puzzle
        if solverithm == 3:
            self.a_star_euclid(puzzle)

    def find_blank_tile(self, curr_state: List[List[int]]) -> List[int]:
        # Create a map to store the coordinates of each number
        num_map = {}
        for i, row in enumerate(curr_state):
            for j, num in enumerate(row):
                num_map[num] = (i, j)
        
        # Get the coordinates of the blank tile (0) and store them in a list
        blank_tile_coords = num_map[0]
        return list(blank_tile_coords)

    def a_star_euclid(self, curr_state: List[List[int]]) -> None:
        h = self.h_euclid(curr_state)
        blank = self.find_blank_tile(curr_state)

        # blank tile is at (0, #)
        if blank[0] == 0:
            if blank[1] == 0 or blank[1] == len(curr_state[0]) - 1:
                # this is a corner
                if blank[1] == 0:
                    # (0,0)
                    0 # #
                    # # #
                    # # #
                    
                    # swap
                    # # #
                    0 # #
                    # # #
                    state1 = [row[:] for row in curr_state]
                    state1[blank[0]][blank[1]], state1[blank[0] + 1][blank[1]] = state1[blank[0] + 1][blank[1]], state1[blank[0]][blank[1]]
                    print_puzzle(state1)

                    # swap
                    # 0 #
                    # # #
                    # # #
                    state2 = [row[:] for row in curr_state]
                    state2[blank[0]][blank[1]], state2[blank[0]][blank[1] + 1] = state2[blank[0]][blank[1] + 1], state2[blank[0]][blank[1]]
                    print_puzzle(state2)
                else:
                    # (0,2)
                    # # 0
                    # # #
                    # # #

                    # swap
                    # 0 #
                    # # #
                    # # #
                    state1 = [row[:] for row in curr_state]
                    state1[blank[0]][blank[1]], state1[blank[0]][blank[1] - 1] = state1[blank[0]][blank[1] - 1], state1[blank[0]][blank[1]]
                    print_puzzle(state1)

                    # swap
                    # # #
                    # # 0
                    # # #
                    state2 = [row[:] for row in curr_state]
                    state2[blank[0]][blank[1]], state2[blank[0] + 1][blank[1]] = state2[blank[0] + 1][blank[1]], state2[blank[0]][blank[1]]
                    print_puzzle(state2)

        # blank tile is at (2, #)
        elif blank[0] == len(curr_state) - 1:
            if blank[1] == 0 or blank[1] == len(curr_state[0]) - 1:
                # this is a corner
                if blank[1] == 0:
                    # (2,0)
                    # # #
                    # # #
                    0 # #

                    # swap
                    # # #
                    0 # #
                    # # #
                    state1 = [row[:] for row in curr_state]
                    state1[blank[0]][blank[1]], state1[blank[0] - 1][blank[1]] = state1[blank[0] - 1][blank[1]], state1[blank[0]][blank[1]]
                    print_puzzle(state1)

                    # swap
                    # # #
                    # # #
                    # 0 #
                    state2 = [row[:] for row in curr_state]
                    state2[blank[0]][blank[1]], state2[blank[0]][blank[1] + 1] = state2[blank[0]][blank[1] + 1], state2[blank[0]][blank[1]]
                    print_puzzle(state2)
                else:
                    # (2,2)
                    # # #
                    # # #
                    # # 0

                    # swap
                    # # #
                    # # #
                    # 0 #
                    state1 = [row[:] for row in curr_state]
                    state1[blank[0]][blank[1]], state1[blank[0]][blank[1] - 1] = state1[blank[0]][blank[1] - 1], state1[blank[0]][blank[1]]
                    print_puzzle(state1)

                    # swap
                    # # #
                    # # 0
                    # # #
                    state2 = [row[:] for row in curr_state]
                    state2[blank[0]][blank[1]], state2[blank[0] - 1][blank[1]] = state2[blank[0] - 1][blank[1]], state2[blank[0]][blank[1]]
                    print_puzzle(state2)

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
                print("currNum", currNum, "x1:", x1, "x2:", x2, "y1:", y1, "y2:", y2, "euclid:", euclid)
        
        print("H:", h)
        return -1

puzzle = [
    [1, 2, 3],
    [4, 8, 5],
    [7, 6, 0]
]

Problem(puzzle, 3)

