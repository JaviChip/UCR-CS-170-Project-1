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

    
    def __init__(self, initialState, goalState = None, heuristic = None):

        self.initialState = initialState

        self.goalState = goalState
        
        self.heuristic = heuristic
