from typing import List


class Problem:
   def __init__(self, puzzle: List[List[int]], algorithm: int) -> None:
       self.puzzle = puzzle
       if algorithm == 2:
           self.a_star_misplaced()


   def print_puzzle(self) -> None:
       pass


   def a_star_misplaced(self) -> None:
       h = self.h_misplaced(self.puzzle)


   def h_misplaced(self, curr_state: List[List[int]]) -> float:
       h = 0
       mapping = {
           1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 0: (2, 2)
       }


       for i in range(len(curr_state)):
           for j in range(len(curr_state)):
               tile = curr_state[i][j]
               if (i, j) != mapping[tile]:
                   h += 1

       return print(int(h))  # Return the count as a float


puzzle = [
   [1, 2, 3],
   [8, 0, 4],
   [7, 6, 5]
]

Problem(puzzle, 2)

