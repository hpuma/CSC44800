# Node class for a tree Node
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def getChildren(self):
    children = []
   
    if self.left != None:
      children.append(self.left)

    if self.right != None:
      children.append(self.right)

    return children
    
  def __str__(self, level=0):
    ret = "\t" * level + repr(self.val) + "\n"
    if self.right != None:
      ret += self.right.__str__(level+1)

    if self.left != None:
      ret += self.left.__str__(level+1)
    
    return ret

  def __repr__(self):
    return str(self.val)
