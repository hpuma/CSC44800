from GraphingAlgorithm import *

# Run BFS or DFS on all trees
def runOnAllTrees(traverseType: str) -> None:
  print(traverseType, "----------------------------")
  for i in range(1,3):
    treeRoot = getTreeRoot(str(i))
    traverseTree(treeRoot, traverseType)

# Main
runOnAllTrees("BFS")
runOnAllTrees("DFS")
