q = ["bob","toa","soh","cah","cosh"]
t=3


def enqueue(item):
  global q
  global t
  if t>=len(q):
    print("Queue is full")
    return False
  else:
    q[t]=item
    tail+=1
    return True

def dequeue():
  global q
  global t
  if t==0:
    print("Queue is empty")
    return False
  else:
    item = q[0]
    q = q[1:]
    t-=1
    return item


class queue:
  class Node:
    data= None
    pointer = None
  head = None
  tail = None
  def enqueue(self,item):
    try:
      newNode = queue.Node()
      newNode.data = item
      if self.head == None:
        self.head = newNode
      else:
        self.tail.pointer = newNode
      self.tail = newNode
      return True
    
    
    
    
    except:
      return False
  def de(self):
    if self.head is not None:
      item=self.head.data
      self.head=self.head.pointer
      return item
    else:
      return None


mq = Queue()
mq.enque("bob")
mq.enque("toa")
print(mq.peek())