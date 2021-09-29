from Node import *

# GRAPH DEFINITIONS
def getTreeRoot(treeNum: str) -> Node:
  # treeNum: 1
  root = None
  node = [Node(i) for i in range(0,9)]
  root = node[0]
  root.setChildren([node[1], node[2]])
  node[1].setChildren([node[3], node[4]])

  # Build the remaining graph for treeNum: 2
  if treeNum == 2:
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
def printTree(root: Node) -> None:
  if root == None:
    return
  
  Nodes = []
  preOrderTraversal(root, Nodes)
  print("Tree Nodes:", Nodes)
  print(root)

  return Nodes

def preOrderTraversal(root: Node, Nodes: list) -> None:
  if root == None or root.children == None:
    return

  Nodes.append(root.val)
  for child in root.getChildren():
    preOrderTraversal(child, Nodes)   
