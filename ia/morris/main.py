#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
from ia.morris.structure import Node as Game
import ia.morris.game as Agent
new_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
player={"white":1, "black":2}
new_game = Game(new_board,player["white"],[3,3],[[],[]])
a = Agent.play(new_game)

pair=0
wins=0
lose=0

for i in a:
    if i.score==0: pair+=1
    if i.score==1: wins+=1
    if i.score==-1: lose+=1

print(pair, wins, lose)
"""new_game.place(0)
print(new_game.left)"""
"""new_game.expand_place()
new_game.child[0].expand_place()
for i in new_game.child[0].child:
    print(i.board)
print("------------")
for i in new_game.child:
    print(i.board)"""