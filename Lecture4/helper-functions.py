import TreeNode from TreeNode


def getTreeRoot(graphType: string) -> TreeNode:
  root = TreeNode(0);

  match graphType:
    case "2":
    case _:
      return null;

  return root
