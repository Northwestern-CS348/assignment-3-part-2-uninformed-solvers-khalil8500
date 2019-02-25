
from solver import *

class SolverDFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Depth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        if self.gm.isWon():
            return True
        self.currentState.= self.gm.getMovables()
        self.currentState = GameState(self.gm.getGameState(), self.currentState.depth+1, )
        if moves:
            for move in moves:
                self.gm.makeMove(move)
                if self.solveOneStep():
                    return True
                self.gm.reverseMove(move)
        return False

class SolverBFS(UninformedSolver):
    def __init__(self, gameMaster, victoryCondition):
        super().__init__(gameMaster, victoryCondition)

    def solveOneStep(self):
        """
        Go to the next state that has not been explored. If a
        game state leads to more than one unexplored game states,
        explore in the order implied by the GameMaster.getMovables()
        function.
        If all game states reachable from a parent state has been explored,
        the next explored state should conform to the specifications of
        the Breadth-First Search algorithm.

        Returns:
            True if the desired solution state is reached, False otherwise
        """
        ### Student code goes here
        if self.gameMaster.getGameState() == self.victoryCondition:
            return True
        moves = self.gameMaster.getMovables()
        if moves:
            for move in moves:
                self.gameMaster.makeMove(move)
                if self.gameMaster.getGameState() == self.victoryCondition:
                    return True
                self.gameMaster.reverseMove(move)
            for move in moves:
                self.gameMaster.makeMove(move)
                if self.solveOneStep():
                    return True
                self.gameMaster.reverseMove(move)
        return False

