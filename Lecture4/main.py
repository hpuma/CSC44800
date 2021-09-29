from GraphingAlgorithm import *
from helpers import *

# Run BFS or DFS on all trees, 1 <= traverseType <= 2
def startSearch(traverseType: str, graphNum: int = 0 ) -> None:
  print(traverseType, "----------------------------")
  if graphNum:
    treeRoot = getTreeRoot(graphNum)
    traverseTree(treeRoot, traverseType)
  else:
     for i in range(1,3):
      treeRoot = getTreeRoot(i)
      traverseTree(treeRoot, traverseType)



# Run BFS and DFS on all graphs
# startSearch("BFS")
# startSearch("DFS")

# Run BFS and DFS on specific graphs
startSearch("BFS", 2)
