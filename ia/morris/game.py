#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
import ia.morris.structure


def play(root):
    result = 0
    playing = True
    # while playing:

    openlist = []
    openlist.append(root)
    closedlist = []
    lastSolutions = []
    p_lastSolution=[]
    current_node = None
    while len(openlist) > 0:  # placing
        current_node = openlist[0]
        del openlist[0]
        closedlist.append(current_node)
        if (current_node.left[0] != 0 or current_node.left[1] != 0):
            current_node.expand_place()

            for node in current_node.child:
                if not (in_list(openlist, node) and in_list(closedlist, node) and in_list(lastSolutions, node)):
                    if (node.left == [0, 0] or node.left == [0, 1]):
                        node.init_score()
                        if (node.left == [0, 1] and node.score == 0):
                            openlist.append(node)
                        else:
                            if node.left == [0, 0]:
                                lastSolutions.append(node)
                            else:
                                p_lastSolution.append(node)
                    else:
                        openlist.append(node)

    possible_placing_results=lastSolutions + p_lastSolution
    print("fatta la prima fase")
    evaluated = False

    analyized=[]
    parents = lastSolutions.copy() #qui devo passare al inizio solo [0,0] e poi sommare [0,1] a quello che ho trovato dopo
    new_parents = p_lastSolution.copy()
    while not evaluated:
        print("for deep:" + str(parents[0].left))
        for node in parents:

            """if node.parent.player==1 and node.score==1:
                node.parent.score=1
            if node.parent.player==2 and node.score==-1:
                node.parent.score=-1"""
            node.parent.scores.append(node.score)
            if node.parent in analyized:
                continue
            new_parents.append(node.parent)
            analyized.append(node.parent)

        parents = new_parents
        for node in parents:
            if(node.player==1):
                if node.scores!=[]:
                    node.score = max(node.scores)
            if(node.player==2):
                if node.scores!=[]:
                    node.score = min(node.scores)
        new_parents = []
        if len(parents)==1 :
            evaluated = True
        print(len(parents))
    #return lastSolutions + p_lastSolution

    playing=True
    game=[]
    game.append(root)
    while playing:
        current_node=game[-1]
        active_player=current_node.player

        if active_player==1:    #maximize
            candidates=[]
            for node in current_node.child:
                candidates.append(node)
            candidates.sort(key=lambda node: node.score, reverse=True)
            print(candidates[0].show())
            game.append(candidates[0])

        if active_player==2:    #maximize
            candidates=[]
            move = int(input("next move?"))
            next_node=None
            for node in current_node.child:
                print(node.positions[active_player - 1])
                if move in node.positions[active_player-1]:
                    next_node= node
            print(next_node)
            game.append(next_node)
            """for node in current_node.child:
                candidates.append(node)
            candidates.sort(key=lambda score: node.score)
            print(candidates[0].show())
            game.append(candidates[0])"""

        if game[-1] in possible_placing_results:
            return game


def in_list(list, node):
    for i in list:
        if i.board == node.board:
            return True
    return False
