class Stack:
  class Node:
    data = None
    pointer = None

  top = None
  def push(self,data):
    try:
      new_node = Stack.Node()
      new_node.data = data
      new_node.pointer = self.top
      return True
    
    
    except:
      return False
    
    
  def pop(self):
    if self.top is not None:
      popped = self.top.data
      self.top = self.top.pointer
      return popped
    else:
      return None
    
  def peek(self):
    if self.top is not None:
      return self.top.data
    else:
      return None
    





items = ["LON","BER","ROM"]
s = Stack()
for i in range(len(items)):
  print(s.push(items[i]))
  s.push(items[i])

print("Item at top", s.peek())