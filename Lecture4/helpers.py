from TreeNode import TreeNode

# Create multiple custom graphs
def getTreeRoot(treeNum: str) -> TreeNode:
  # treeNum: 1
  root = None
  node = [TreeNode(i) for i in range(0,9)]
  root = node[0]
  root.setChildren([node[1], node[2]])
  node[1].setChildren([node[3], node[4]])

  # Build the remaining graph for treeNum: 2
  if treeNum == "2":
    node[2].setChildren([node[5], node[6]])
    node[4].setChildren([node[7], node[8]])

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
  if root.children != None:
     for child in root.getChildren():
        if child != None:
          preOrderTraversal(child, treeNodes)    
  return
