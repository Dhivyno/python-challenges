buffer = 0
class Node:
  def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
  def insert(self, data):
    if self.data is not None: 
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.insert(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.insert(data)
    else:
      self.data = data
  def PrintTree(self):
    if self.left is not None:
      self.left.PrintTree()
    print(self.data)
    if self.right is not None:
      self.right.PrintTree()
  def find(self, val):
    if self.data > val:
      if self.left is not None:
        self.left.find(val)
      else: 
        print("Not found")
    elif self.data < val:
      if self.right is not None:
        self.right.find(val)
      else:
        print("Not found")
    else:
      print("Found", val)
  def findDeep(self):
    if self.right is not None:
      return self.right.findDeep()
    else:
      buffer = self.data
      self.data = None
      return buffer
  def delete(self, val):
    buffer1 = self.findDeep()
    print(buffer1)
    if self.data > val:
      print("Higher")
      if self.left is not None:
        self.left.delete(val)
      else: 
        print("Not found")
    elif self.data < val:
      if self.right is not None:
        self.right.delete(val)
      else:
        print("Not found")
    else:
      print("Found")
      self.data = buffer1
    
    
      

root = Node(10)
root.insert(9)
root.insert(8)
root.insert(12)
root.insert(14)
root.insert(3)
root.find(3)
root.delete(3)
root.PrintTree()