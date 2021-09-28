# Node class for a tree Node
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def getChildren(self):
    children = []
   
    if(self.right != None):
      children.append(self.right)

    if(self.left != None):
      children.append(self.left)
    
    return children
    
  def __str__(self, level=0):
    ret = "\t" * level + repr(self.val) + "\n"
    for child in self.getChildren():
      ret += child.__str__(level+1)
    return ret

  def __repr__(self):
    return '<TreeNode>'