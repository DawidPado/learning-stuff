#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify
from ia.puzzle8.structure import Node


def breath_first_search(root):
    PathToSolution = []
    OpenList = []  # list that i can expand
    ClosedList = []  # list already expanded

    OpenList.append(root)
    goalfound = False

    while not goalfound and len(OpenList) > 0:
        currentNode = OpenList[0]

        del OpenList[0]
        #check(currentNode, ClosedList, OpenList)
        ClosedList.append(currentNode)
        #print(len(OpenList), len(ClosedList))
        #print(currentNode.puzzle)
        currentNode.expand()

        for node in currentNode.children:
            if node.isGoal():
                print("Goal found!")
                print("num of steps analyzed: " + str(len(ClosedList)))
                PathToSolution.append(node)
                find_path(PathToSolution)
                return PathToSolution

            in_closednode = in_list(ClosedList,node)
            in_opennode = in_list(OpenList,node)
            if (not in_closednode) and (not in_opennode):
                OpenList.append(node)


def depth_first_search(root):
    PathToSolution = []
    OpenList = []  # list that i can expand
    ClosedList = []  # list already expanded

    OpenList.append(root)
    goalfound = False

    while not goalfound and len(OpenList) > 0:
        currentNode = OpenList[-1]

        del OpenList[-1]
        #check(currentNode, ClosedList, OpenList)
        ClosedList.append(currentNode)
        #print(len(OpenList), len(ClosedList))
        #print(currentNode.puzzle)
        currentNode.expand()

        for node in currentNode.children:
            if node.isGoal():
                print("Goal found!")
                print("num of steps analyzed: " + str(len(ClosedList)))
                PathToSolution.append(node)
                find_path(PathToSolution)
                return PathToSolution

            in_closednode = in_list(ClosedList,node)
            in_opennode = in_list(OpenList,node)
            if (not in_closednode) and (not in_opennode):
                OpenList.append(node)


def best_first_search(root,heuristic):
    PathToSolution = []
    OpenList = []  # list that i can expand
    ClosedList = []  # list already expanded

    OpenList.append(root)
    goalfound = False

    while not goalfound and len(OpenList) > 0:
        currentNode = OpenList[0]
        print(ClosedList)
        del OpenList[0]
        #check(currentNode, ClosedList, OpenList)
        ClosedList.append(currentNode)
        #print(len(OpenList), len(ClosedList))
        #print(currentNode.puzzle)
        currentNode.expand()

        for node in currentNode.children:
            if node.isGoal():
                print("Goal found!")
                print("num of steps analyzed: " + str(len(ClosedList)))
                PathToSolution.append(node)
                find_path(PathToSolution)
                return PathToSolution

            in_closednode = in_list(ClosedList,node)
            in_opennode = in_list(OpenList,node)
            if (not in_closednode) and (not in_opennode):
                OpenList.append(node)
        if heuristic == "manhattan":
            OpenList.sort(key=lambda node: node.manhattan_d())
        else:
            OpenList.sort(key=lambda node: node.good_position(),reverse=True)

def A_STAR(root,heuristic):
    PathToSolution = []
    OpenList = []  # list that i can expand
    ClosedList = []  # list already expanded

    OpenList.append(root)
    goalfound = False

    while not goalfound and len(OpenList) > 0:
        currentNode = OpenList[0]
        del OpenList[0]
        #check(currentNode, ClosedList, OpenList)
        ClosedList.append(currentNode)
        #print(len(OpenList), len(ClosedList))
        #print(currentNode.puzzle)
        currentNode.expand()

        for node in currentNode.children:
            if node.isGoal():
                print("Goal found!")
                print("num of steps analyzed: " + str(len(ClosedList)))
                PathToSolution.append(node)
                find_path(PathToSolution)
                return PathToSolution

            in_closednode = in_list(ClosedList,node)
            in_opennode = in_list(OpenList,node)
            if (not in_closednode) and (not in_opennode):
                OpenList.append(node)
        if heuristic == "manhattan":
            OpenList.sort(key=lambda node: node.manhattan_d() + node.path)
        else:
            OpenList.sort(key=lambda node: node.good_position() + node.path ,reverse=True)

def in_list(list, node):
    for i in list:
        if i.puzzle == node.puzzle:
            return True
    return False


def find_path(PathToSolution):
    """
    :param PathToSolution: array that contains node of the solution
    :return: array that contains the path from start to final problem
    """
    has_parent = True
    while has_parent:
        if PathToSolution[len(PathToSolution) - 1].parent != None:
            PathToSolution.append(PathToSolution[len(PathToSolution) - 1].parent)
        else:
            has_parent = False
    PathToSolution.reverse()


def check(node,c,o):
    """
    method made for debugging
    :param node: current node
    :param c:  if node is in closed list
    :param o: if node is in open list
    :return: true if already exist
    """
    if (in_list(c,node)):
        print("duplicate!")
        return True
    if (in_list(o,node)):
        print("duplicate!")
        return True
    return False


