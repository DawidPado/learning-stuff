#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
import ia.morris.heuristic as heuristic

bot = True


def play(root, bot):
    result = 0
    depth = 3

    possible_placing_results = heuristic.get_heuristic_places(root)

    moving = True
    placing = True
    game = []
    game.append(root)
    if bot:
        while placing:
            current_node = game[-1]
            active_player = current_node.player
            if active_player == 1:  # maximize
                candidates = []
                for node in current_node.child:
                    candidates.append(node)
                candidates.sort(key=lambda node: node.score, reverse=True)
                candidates[0].show()
                game.append(candidates[0])

            if active_player == 2:  # maximize
                candidates = []
                for node in current_node.child:
                    candidates.append(node)
                candidates.sort(key=lambda score: node.score)
                candidates[0].show()
                game.append(candidates[0])

            if game[-1] in possible_placing_results and game[-1].score != 0:
                return game
            if game[-1] in possible_placing_results and game[-1].score == 0:
                break

        while moving:
            current_node = game[-1]
            active_player = current_node.player
            heuristic.get_hueristic_moves(current_node, depth)
            if active_player == 1:  # maximize
                candidates = []
                for node in current_node.child:
                    candidates.append(node)
                candidates.sort(key=lambda node: node.score, reverse=True)
                candidates[0].show()
                print(candidates[0].scores)
                game.append(candidates[0])

            if active_player == 2:  # maximize
                candidates = []
                for node in current_node.child:
                    candidates.append(node)
                candidates.sort(key=lambda node: node.score, reverse=True)
                candidates[0].show()
                print(candidates[0].scores)
                game.append(candidates[0])

            if game[-1].positions[active_player - 1] in game[-1].win_positions:
                return game

        else:
            while placing:
                current_node = game[-1]
                active_player = current_node.player
                if active_player == 1:  # maximize
                    candidates = []
                    for node in current_node.child:
                        candidates.append(node)
                    candidates.sort(key=lambda node: node.score, reverse=True)
                    candidates[0].show()
                    game.append(candidates[0])

                if active_player == 2:  # maximize
                    candidates = []
                    move = int(input("next move?"))
                    next_node = None
                    for node in current_node.child:
                        if move in node.positions[active_player - 1]:
                            next_node = node
                    game.append(next_node)
                    for node in current_node.child:
                        candidates.append(node)
                    candidates.sort(key=lambda score: node.score)
                    candidates[0].show()
                    game.append(candidates[0])

                if game[-1] in possible_placing_results and game[-1].score != 0:
                    return game
                if game[-1] in possible_placing_results and game[-1].score == 0:
                    break

            while moving:
                current_node = game[-1]
                active_player = current_node.player
                heuristic.get_hueristic_moves(current_node, depth)
                if active_player == 1:  # maximize
                    candidates = []
                    for node in current_node.child:
                        candidates.append(node)
                    candidates.sort(key=lambda node: node.score, reverse=True)
                    candidates[0].show()
                    game.append(candidates[0])

                if active_player == 2:  # maximize
                    candidates = []
                    move_from = int(input("next move from?"))
                    move_to = int(input("next move to?"))
                    move = current_node.board.copy()
                    move[move_from] = 0
                    move[move_to] = active_player
                    next_node = None

                    for node in current_node.child:
                        if move == node.board:
                            next_node = node
                    next_node.show()
                    game.append(next_node)

                if game[-1].positions[active_player - 1] in game[-1].win_positions:
                    return game