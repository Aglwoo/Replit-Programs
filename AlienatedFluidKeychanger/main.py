class Node():
  def __init__(self, val):
    self.val = val
    self.next = None

class Linked():
  def __init__(self):
    self.head = None
    self.size = 0

  def addathead(self, val):
    node = Node(val)
    node.next= self.head
    self.head = node
    self.size += 1

  def addinorder(self,item):
    none = Node(item)
    current = self.head
    while current is not None and current.val < item:
      prev = current
      current= current.next
    node.next = prev.next
    prev.next = node
    

  def addattail(self, val):
    current=self.head
    if current == None:
      self.head = Node(val)
    else:
      while current.next is not None:
        current = current.next
      current.next = Node(val)
    self.size+=1

  def output(self):
    current=self.head
    while current is not None:
      print(current.val)
      current = current.next

#  def outputRev(self):
    
linkedlist = Linked()
linkedlist.addathead("LON")
linkedlist.addathead("NYC")
linkedlist.addathead("BOS")
linkedlist.output()