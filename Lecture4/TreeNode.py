# Node class for a tree Node
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def getChildren(self):
    children = List()
    if(self.left != None):
      children.append(self.left)
    
    if(self.right != None):
      children.append(self.right)
    return children
    