# A Node class for a graph
class Node:
  def __init__(self, val):
    self.val = val
    self.children = None

  def setChildren(self, children):
    if not len(children):
      return
    self.children = children

  # Get children if exist, else return empty array  
  def getChildren(self):
    return self.children if self.children != None else []

  def __str__(self, level=0):
    # Print current value and check if we have children if not, then exit early
    ret = "\t" * level + repr(self.val) + "\n"
    if self.children == None:
      return ret
      
    # Making a copy of children but in reverse order (for output)
    reversedChildren = self.getChildren()[::-1]
    for child in reversedChildren:
      ret += child.__str__(level + 1)
      
    return ret

  def __repr__(self):
    return str(self.val) if self.val != None else "NONE"
