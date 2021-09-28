from TreeNode import TreeNode
# Create multiple custom graphs
def getTreeRoot(graphType: str) -> TreeNode:
  root = None
  root = TreeNode("A")
  if graphType == "1":
    root.left = TreeNode("B")
    root.right = TreeNode("C")

    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")

    root.right.left = TreeNode("F")
    root.right.right = TreeNode("G")

    root.left.right.left = TreeNode("H")
    root.left.right.right = TreeNode("I")
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
