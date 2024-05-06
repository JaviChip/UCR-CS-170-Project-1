from node import Node

class Problem:
    
    def __init__(self, initialState, goalState = None, heuristic = None):

        self.initialState = initialState

        self.goalState = goalState
        
        self.heuristic = heuristic
