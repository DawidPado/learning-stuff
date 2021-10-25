#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
def get_heuristic_places(root):
    openlist = [root]
    lastSolutions = []
    p_lastSolution = []
    pairs = []
    # ---building tree for placing--#
    while len(openlist) > 0:  # placing
        current_node = openlist[0]
        del openlist[0]
        if current_node.left[0] != 0 or current_node.left[1] != 0:
            current_node.expand_place()

            for node in current_node.child:
                if not (current_node in p_lastSolution and current_node in lastSolutions):
                    if node.left == [0, 0] or node.left == [0, 1]:
                        node.init_score()
                        if node.left == [0, 1] and node.score == 0:
                            openlist.append(node)
                        else:
                            if node.left == [0, 0]:
                                if node.score == 0:
                                    pairs.append(node)
                                lastSolutions.append(node)
                            else:
                                p_lastSolution.append(node)
                    else:
                        openlist.append(node)
    # --end building tree--#

    # --heuristic for placing--#
    possible_placing_results = lastSolutions + p_lastSolution
    evaluated = False
    for node in pairs:
        get_hueristic_moves(node, 1)
    analyized = []
    parents = lastSolutions.copy()
    new_parents = p_lastSolution.copy()
    for node in parents:
        node.score *= 10  # win with 3moves
    for node in new_parents:
        node.score *= 20  # win with 2moves

    while not evaluated:
        # print("for deep:" + str(parents[0].left))
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
            if node.player == 1:
                if node.scores:
                    node.score = max(node.scores)
            if node.player == 2:
                if node.scores:
                    node.score = min(node.scores)
        # --end heuristic for moves--#
        new_parents = []
        if len(parents) == 1:
            evaluated = True

    return possible_placing_results


def get_hueristic_moves(root, depth):
    # --building tree for moves if pair during placing#
    nodes = [[root]]
    lastmoves = []
    score = 4

    """for i in range(depth + 1):
        lastmoves.append([])

    for i in range(depth + 1):
        nodes.append([])
        while len(nodes[i]) > 0:
            current_node = nodes[i][0]
            current_node.expand_move()
            del nodes[i][0]
            current_node.init_score()
            if current_node.score == 0:
                for node in current_node.child:
                    if i == depth + 1:
                        lastmoves[i].append(node)
                    else:
                        nodes[i + 1].append(node)
            else:
                current_node.score = current_node.score * (score - i)
                lastmoves[i].append(current_node)
        # --end building tree--#"""



#TODO profondita almeno 2
    root.expand_move()
    to_expand=[]
    for node in root.child:
        node.init_score()
        if node.score==0:
            to_expand.append(node)
        """else:
            i.parent.scores.append(i.score)"""

    for node in to_expand:
        node.expand_move()
        for child in node.child:
            child.init_score()
            node.scores.append(child.score)


############
    for node in root.child:
        if node.score==0:
            if node.player==1:
                node.score=max(node.scores)
                root.scores.append(node.score)
            else:
                node.score=min(node.scores)
        root.scores.append(node.score)


    if root.player == 1:
        root.score = max(root.scores)
    else:
        root.score = min(root.scores)


    # --heuristic for moves--#
    """lastmoves_nodes = lastmoves.copy()
    while len(lastmoves_nodes) > 0:
        current_node = lastmoves_nodes[0]
        del lastmoves_nodes[0]
        current_node.parent.scores.append(current_node.score)"""

    """nodes = []
    for i in range(depth + 1):
        lastmoves.append([])"""

    """nodes=lastmoves
    nodes.reverse()
    for i in range(depth + 1):
        nodes[i]+=lastmoves[i]
        while len(nodes[i]) > 0:
            current_node = nodes[i][0]
            del nodes[i][0]
            current_node.parent.scores.append(current_node.score)
            # if not current_node in pairs:
            if current_node.player == 1:
                if current_node.scores != []:
                    current_node.score = max(current_node.scores)
            if current_node.player == 2:
                if current_node.scores != []:
                    current_node.score = min(current_node.scores)
            if not current_node in nodes[i + 1]:
                nodes.append(current_node)"""

    # --end heuristic for moves--#
