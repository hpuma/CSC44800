from TreeNode import *
from helpers import * 

def BFS(root):
  curr = root
  frontier = [curr]
  explored = []
  i = 0
  while len(frontier):
    curr = frontier.pop(0)
    frontier += curr.getChildren()

    explored.append(curr)
    printTrackingLists(frontier, explored, i)
    i+=1

# For graphs 1 and 2
for i in range(1,3):
  BFS( getTreeRoot(str(i)))
