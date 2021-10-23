#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify

class Node:
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    0--0--0
    |\ | /|
    0--0--0
    |/ | \|
    0--0--0
    """
    left = [3, 3]
    players = {1: 2, 2: 1}
    player = 0
    parent = None
    child = []
    score = 0
    scores=[]
    positions=[[],[]]

    def __init__(self, board, player, left, positions):
        self.board = board
        self.player = player
        self.left = left
        self.child = []
        self.scores=[]
        self.positions= positions

    def place(self, position):
        board = self.board.copy()
        positions=self.positions.copy()
        new_player = self.players[self.player]
        left = self.left.copy()

        if self.board[position] == 0:
            board[position] = self.player
            left[self.player - 1] = self.left[self.player - 1] - 1
            positions[self.player - 1] = self.positions[self.player - 1].append(position)

            new_child = Node(board, new_player, left, positions)
            new_child.calculate_postions()

            self.child.append(new_child)
            new_child.parent = self

    def expand_place(self):
        for i in range(9):
            self.place(i)

    def move_down(self, position):
        if position < 6:
            if self.board[position + 3] == 0:
                new_child = Node(self.board.copy(), self.players[self.player])

                new_child.board[position + 3] = self.player
                new_child.board[position] = 0

                new_child.parent = self
                self.child.append(new_child)

    def move_up(self, position):
        if position > 2:
            if self.board[position - 3] == 0:
                new_child = Node(self.board.copy(), self.players[self.player])

                new_child.board[position - 3] = self.player
                new_child.board[position] = 0

                new_child.parent = self
                self.child.append(new_child)

    def move_right(self, position):
        if position % 3 != 2:
            if self.board[position + 1] == 0:
                new_child = Node(self.board.copy(), self.players[self.player])

                new_child.board[position + 1] = self.player
                new_child.board[position] = 0

                new_child.parent = self
                self.child.append(new_child)

    def move_left(self, position):
        if position % 3 != 0:
            if self.board[position - 1] == 0:
                new_child = Node(self.board.copy(), self.players[self.player])

                new_child.board[position - 1] = self.player
                new_child.board[position] = 0

                new_child.parent = self
                self.child.append(new_child)

    def move_center(self, position):
        if (position not in [1, 3, 5, 7]):
            if self.board[4] == 0:
                new_child = Node(self.board.copy(), self.players[self.player])

                new_child.board[4] = self.player
                new_child.board[position] = 0

                new_child.parent = self
                self.child.append(new_child)

    def expand_move(self):
        positions = self.board.index(self.player)
        for pawn in positions:
            self.move_center(pawn)
            self.move_up(pawn)
            self.move_right(pawn)
            self.move_down(pawn)
            self.move_left(pawn)

    def end_placing(self):
        if self.left != [0, 0]:
            return False
        return True

    def init_score(self):
        """
        :return: if 1 wins:1 , if 1 lose:-1, if pair:0
        """
        score = 0
        positions = self.positions
        """board=self.board
        p1_index=[]
        p2_index=[]
        for i in range(9):
            if board[i]==1:
                p1_index.append(i)
            if board[i]==2:
                p2_index.append(i)"""
        if positions[0] in [[0, 1, 2],[0, 3, 6],[6, 7, 9],[3, 5, 8],[1, 4, 7],[3, 4, 5],[0, 4, 8],[2,4,6]]:
            score = 1
        if positions[1] in [[0, 1, 2],[0, 3, 6],[6, 7, 9],[3, 5, 8],[1, 4, 7],[3, 4, 5],[0, 4, 8],[2,4,6]]:
            score = -1
        self.score=score

    def end_game(self):
        if self.score == 1 or self.score == -1: #and self.end_placing() == True
            return True
        else:
            return False

    def show(self):
        b=self.board
        print(str(b[0])+"--"+str(b[1])+"--"+str(b[2]))
        print("|\ | /|")
        print(str(b[3]) + "--" + str(b[4]) + "--" + str(b[5]))
        print("|/ | \|")
        print(str(b[6]) + "--" + str(b[7]) + "--" + str(b[8]))
        print()

    def calculate_postions(self):
        p1_index = []
        p2_index = []
        board = self.board
        for i in range(9):
            if board[i] == 1:
                p1_index.append(i)
            if board[i] == 2:
                p2_index.append(i)
        self.positions=[p1_index,p2_index]

    """def store_score(self):
        self.score=self.score()"""