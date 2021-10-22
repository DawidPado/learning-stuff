#  Copyright (c) 2021. Code made by Dawid Pado free to use and change

class Node:
    parent = None
    children = []
    puzzle = []
    index = None
    coll = 3
    goal=[1,2,3,4,5,6,7,8,0]
    score=0
    path=0
    def __init__(self, puzzle):
        """
        :param puzzle: puzzle in the actual state
        """
        self.puzzle = puzzle

    def isGoal(self):
        """
        :return: True if puzzle is complete, False if is not ordered yet
        """
        complete = True
        if self.puzzle != self.goal:
            complete=False
        return complete

    def MoveToRight(self):
        index = self.index
        puzzle = self.puzzle

        if index % self.coll != (self.coll - 1):
            """
            If i am on position 2,5,8 i can move empty puzzle to the right!
            """
            child_puzzle = Node(puzzle.copy())
            # +1 because i move (0), one pos. form initial position in the array

            child_puzzle.path=self.path+1
            # path from the root to the new node

            child_puzzle.puzzle[index + 1] = 0
            child_puzzle.puzzle[index] = puzzle[index + 1]
            # switching values
            self.children.append(child_puzzle)
            child_puzzle.parent=self
            # appending nodes in the tree

    def MoveToLeft(self):
        index = self.index
        puzzle = self.puzzle

        if index % self.coll != 0:
            """
            If i am on position 0,3,6 i can move empty puzzle to the left!
            """
            child_puzzle = Node(puzzle.copy())
            # -1 because i move (0), one pos. form initial position in the array

            child_puzzle.path = self.path + 1
            # path from the root to the new node

            child_puzzle.puzzle[index - 1] = 0
            child_puzzle.puzzle[index] = puzzle[index - 1]
            # switching values
            self.children.append(child_puzzle)
            child_puzzle.parent=self
            # appending nodes in the tree

    def MoveToUp(self):
        index = self.index
        puzzle = self.puzzle

        if index > self.coll-1:
            """
            If i am on position 0,1,2 i can move empty puzzle to the up!
            """
            child_puzzle = Node(puzzle.copy())
            # -3 because i move (0), one pos. form initial position in the array

            child_puzzle.path = self.path + 1
            # path from the root to the new node

            child_puzzle.puzzle[index - self.coll] = 0
            child_puzzle.puzzle[index] = puzzle[index - self.coll]
            # switching values
            self.children.append(child_puzzle)
            child_puzzle.parent=self
            # appending nodes in the tree

    def MoveToDown(self):
        index = self.index
        puzzle = self.puzzle

        if index < self.coll*(self.coll-1):
            """
            If i am on position 6,7,8 i can move empty puzzle to the down!
            """
            child_puzzle = Node(puzzle.copy())
            # +3 because i move (0), one pos. form initial position in the array

            child_puzzle.path = self.path + 1
            # path from the root to the new node

            child_puzzle.puzzle[index + self.coll] = 0
            child_puzzle.puzzle[index] = puzzle[index + self.coll]
            # switching values
            self.children.append(child_puzzle)
            child_puzzle.parent=self
            # appending nodes in the tree

    def describe(self):
        pos = 0
        row = ""
        for i in range(self.coll):
            for i in range(self.coll):
                row += str(self.puzzle[pos]) + " "
                pos += 1
            row += "\n"
        print(row)

    def expand(self):
        self.index = self.puzzle.index(0)

        self.MoveToRight()
        self.MoveToLeft()
        self.MoveToUp()
        self.MoveToDown()

    def manhattan_d(self):
        tot = 0
        for pos in range(self.coll * self.coll):
            tot += abs((self.puzzle.index(pos) % 3) - (self.goal.index(pos) % 3)) + abs(
                (self.puzzle.index(pos) // 3) - (self.goal.index(pos) // 3))
        self.score = tot
        return tot

    def good_position(self):
        tot = 0
        for pos in range(self.coll * self.coll):
            if self.puzzle[pos]==self.goal[pos]:
                tot+=1
        self.score = tot
        return tot