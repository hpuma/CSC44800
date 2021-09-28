from TreeNode import *
from helpers import * 

def printTrackingLists(frontier: list, explored: list, iteration: int) -> None:
  print("i = ", iteration)
  print("Frontier:\t", frontier)
  print("Explored:\t", explored, end="\n\n")

def traverseTree(root, traverseType: str) -> None:
  curr = root
  frontier = [curr]
  explored = []
  i = 0

  isBFS = traverseType == "BFS"
  while len(frontier):
    curr = frontier.pop(0) if isBFS else frontier.pop()
    frontier += curr.getChildren()
    explored.append(curr)
    printTrackingLists(frontier, explored, i)
    i+=1
