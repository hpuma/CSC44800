from TreeNode import TreeNode
# Create multiple custom graphs
def getTreeRoot(graphType: str) -> TreeNode:
  root = None
  root = TreeNode(1)
  if graphType == "1":
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.left.right.left = TreeNode(8)
    root.left.right.right = TreeNode(9)
  else:
    root = None

  printTree(root)
  return root

'''
With a given tree root node
  1. Print all nodes using preorder traversal
  2. Print Tree using preorder traversal
'''
def printTree(root: TreeNode) -> None:
  treeNodes = []
  preOrderTraversal(root, treeNodes)
  print("Tree Nodes:", treeNodes)
  print(root)

  return treeNodes

def preOrderTraversal(root: TreeNode, treeNodes: list) -> None:
  if root is None:
    return

  treeNodes.append(root.val)
  preOrderTraversal(root.left, treeNodes)
  preOrderTraversal(root.right, treeNodes)
  return


def printTrackingLists(frontier: list, explored: list, iteration: int) -> None:
  print("i = ", iteration)
  print("Frontier:\t", frontier)
  print("Explored:\t", explored, end="\n\n")
