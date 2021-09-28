from TreeNode import TreeNode

# Create multiple custom graphs
def getTreeRoot(treeNum: str) -> TreeNode:
  root = None
  root = TreeNode(0)
  root.left = TreeNode(1)
  root.right = TreeNode(2)

  if treeNum == "1":
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
  elif treeNum == "2":
    root.left = TreeNode(1)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
  else:
    root = None

  print("TREE NUMBER:\t", treeNum)
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
