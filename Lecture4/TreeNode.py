# Node class for a tree Node
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.children = None

  def setChildren(self, children):
    if not len(children):
      return
    self.children = children

  def getChildren(self):
    return self.children if self.children != None else []

    
  def __str__(self, level=0):
    ret = "\t" * level + repr(self.val) + "\n"
    
    if self.children != None:
      reversedChildren = self.getChildren()[::-1]
      for child in reversedChildren:
        if child != None:
          ret += child.__str__(level+1)    
    return ret

  def __repr__(self):
    return str(self.val)
