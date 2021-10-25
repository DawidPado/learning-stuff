#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
from ia.morris.structure import Node as Game
import ia.morris.game as Agent

new_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player = {"white": 1, "black": 2}
new_game = Game(new_board, player["white"], [3, 3], [[], []])
a = Agent.play(new_game, True)
score = a[len(a) - 1].score
if score > 0:
    print("white won")
else:
    print("black won")
