from TreeNode import TreeNode

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


def printTree(root: TreeNode) -> None:
    answer = []
    print("Printing Tree:")
    inorderTraversal(root, answer)
    print(answer)
    return answer

def inorderTraversal(root: TreeNode, answer: list) -> None:
    if root is None:
      return
    inorderTraversal(root.left, answer)
    answer.append(root.val)
    inorderTraversal(root.right, answer)
    return

