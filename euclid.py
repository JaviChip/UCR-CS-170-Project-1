from typing import List
from math import sqrt

class Problem:
    def __init__(self, puzzle: List[List[int]], algorithm: int) -> None:
        self.puzzle = puzzle
        if algorithm == 3:
            self.a_star_euclid()

    def print_puzzle(self) -> None:
        pass

    def a_star_euclid(self) -> None:
        h = self.h_euclid(self.puzzle)

    def h_euclid(self, curr_state: List[List[int]]) -> float:
        h = 0
        mapping = {
            1: (0, 0), 2: (0, 1), 3: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            7: (2, 0), 8: (2, 1), 0: (2, 2)
        }

        for i in range(len(curr_state)):
            for j in range(len(curr_state)):
                curr_num = curr_state[i][j]
                x2, y2 = mapping[curr_num]
                x1, y1 = i, j
                
                euclid = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                h += euclid
                print(f"currNum {curr_num} x1: {x1} x2: {x2} y1: {y1} y2: {y2} euclid: {euclid}")
        
        print(f"H: {h}")
        return -1

puzzle = [
    [1, 2, 0],
    [4, 8, 0],
    [7, 6, 5]
]

Problem(puzzle, 3)
