#  Copyright (c) 2021. code created by Dawid Pado, free to use and modify

from ia.puzzle8.structure import Node
import ia.puzzle8.puzzle as solver

p=[2,4,3,
   1,5,6,
   7,8,0]

node = Node(p)
node1 = Node(p)
#print(len(node.children))

"------------"
print("best fs:")
result = solver.A_STAR(node1,"manhattan")
print("moves:" + str(len(result)))
for i in result:
    i.describe()

"""print("breath fs:")
result1=solver.breath_first_search(node)
print("moves:" + str(len(result)))
for i in result1:
    i.describe()"""
"------------"

