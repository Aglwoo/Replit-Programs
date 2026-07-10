  #shopQ = ['Helen', 'Adam', 'John', 'Pete', '', '']

  def shuffle(shopQ):
    customer = shopQ[0]
    shopQ = shopQ[1:] + [""]
    return customer,shopQ

  #customer,shopQ=shuffle(shopQ)
  #print(shopQ)

  #import random
  #table=['A','B','C','D','E','F']

  def rotate(table):
    rotation=random.randint(1,6)
    table=table[-rotation:]+table[0:6-rotation]
    return table
  #print(rotate(table))


  #        head                      tail
  shopQ = ['Helen', 'Adam', 'John', 'Pete', '', '']

  def addCust(name,shopQ):
    shopQ=shopQ[:-shopQ.count("")]+[name]+[""]*(shopQ.count("")-1)
    return shopQ
  print(addCust("JOHNNY",shopQ))

  def removeCust(shopQ):
    return shopQ[1:]+[""]

  print(removeCust(shopQ))



def bubbleSort(shopQ):
  n = len(shopQ)
  for i in range(n):
    for j in range(0, n - i - 1):
      if shopQ[j] > shopQ[j + 1]:
        shopQ[j], shopQ[j + 1] = shopQ[j + 1], shopQ[j]
  return shopQ
  print(bubbleSort(shopQ))