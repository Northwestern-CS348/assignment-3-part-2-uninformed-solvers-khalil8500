from game_master import GameMaster
from read import *
from util import *

class TowerOfHanoiGame(GameMaster):

    def __init__(self):
        super().__init__()
        
    def produceMovableQuery(self):
        """
        See overridden parent class method for more information.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?disk ?init ?target)')

    def getGameState(self):
        """
        Returns a representation of the game in the current state.
        The output should be a Tuple of three Tuples. Each inner tuple should
        represent a peg, and its content the disks on the peg. Disks
        should be represented by integers, with the smallest disk
        represented by 1, and the second smallest 2, etc.

        Within each inner Tuple, the integers should be sorted in ascending order,
        indicating the smallest disk stacked on top of the larger ones.

        For example, the output should adopt the following format:
        ((1,2,5),(),(3, 4))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### student code goes here
        p1 = self.kb.kb_ask(Fact(Statement(["on", "?disk", "peg1"])))
        if p1:
            temp = []
            for i in p1:
                temp.append(int(i.bindings_dict["?disk"][4:5]))
            temp.sort()
            p1 = tuple(temp)
        else:
            p1= tuple()
        p2 = self.kb.kb_ask(Fact(Statement(["on", "?disk", "peg2"])))
        if p2:
            temp = []
            for i in p2:
                temp.append(int(i.bindings_dict["?disk"][4:5]))
            temp.sort()
            p2 = tuple(temp)
        else:
            p2 = tuple()
        p3 = self.kb.kb_ask(Fact(Statement(["on", "?disk", "peg3"])))
        if p3:
            temp = []
            for i in p3:
                temp.append(int(i.bindings_dict["?disk"][4:5]))
            temp.sort()
            p3 = tuple(temp)
        else:
            p3 = tuple()

        return tuple([p1, p2, p3])

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable disk1 peg1 peg3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here

        terms = movable_statement.terms
        disk = terms[0]
        p1 = terms[1]
        p2 = terms[2]
        self.kb.kb_retract(Fact(movable_statement))
        self.kb.kb_retract(Fact(Statement(["on", disk, p1])))

        disk_on = self.kb.kb_ask(Fact(Statement(["on", disk, "?disk"])))
        if disk_on:
            val = disk_on[0].bindings_dict["?disk"]
            self.kb.kb_retract(Fact(Statement(["on", disk, val])))
            self.kb.kb_retract(Fact(Statement(["tops", disk, p1])))
            self.kb.kb_assert(Fact(Statement(["tops", val, p1])))

        self.kb.kb_retract(Fact(Statement(["empty", p2])))

        self.kb.kb_assert(Fact(Statement(["tops", disk, p2])))
        self.kb.kb_assert(Fact(Statement(["on", disk, p2])))

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[2], sl[1]]
        self.makeMove(Statement(newList))

class Puzzle8Game(GameMaster):

    def __init__(self):
        super().__init__()

    def produceMovableQuery(self):
        """
        Create the Fact object that could be used to query
        the KB of the presently available moves. This function
        is called once per game.

        Returns:
             A Fact object that could be used to query the currently available moves
        """
        return parse_input('fact: (movable ?piece ?initX ?initY ?targetX ?targetY)')

    def getGameState(self):
        """
        Returns a representation of the the game board in the current state.
        The output should be a Tuple of Three Tuples. Each inner tuple should
        represent a row of tiles on the board. Each tile should be represented
        with an integer; the empty space should be represented with -1.

        For example, the output should adopt the following format:
        ((1, 2, 3), (4, 5, 6), (7, 8, -1))

        Returns:
            A Tuple of Tuples that represent the game state
        """
        ### Student code goes here
        pass

    def makeMove(self, movable_statement):
        """
        Takes a MOVABLE statement and makes the corresponding move. This will
        result in a change of the game state, and therefore requires updating
        the KB in the Game Master.

        The statement should come directly from the result of the MOVABLE query
        issued to the KB, in the following format:
        (movable tile3 pos1 pos3 pos2 pos3)

        Args:
            movable_statement: A Statement object that contains one of the currently viable moves

        Returns:
            None
        """
        ### Student code goes here
        pass

    def reverseMove(self, movable_statement):
        """
        See overridden parent class method for more information.

        Args:
            movable_statement: A Statement object that contains one of the previously viable moves

        Returns:
            None
        """
        pred = movable_statement.predicate
        sl = movable_statement.terms
        newList = [pred, sl[0], sl[3], sl[4], sl[1], sl[2]]
        self.makeMove(Statement(newList))
