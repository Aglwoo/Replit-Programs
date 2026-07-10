print("""stack = ["LON", "BER", "PAR", "", "", "", ""]

top = 3

def push(arr,top,item):
  if top == len(stack):
    return "Stack Overflow"
  else:
    stack[top] = item
    top += 1
    return stack

def pop(arr,top,item):

pu""")
Queue = ["Hamza", "Ahmed", "Mohammed", "Ali", "Dom",""]
def bob(Queue):
  customer = Queue[0]
  Queue = Queue[1:]+[""]
  print(Queue)
#bob(Queue)


Table = "A","B","C","D","E","F"
move = input("Tables moved")
snum = len(Table)-int(move)
def job(Table,snum):
  for i in range(snum):
    temp = Table[i+1]
    if i+1 != 6:
      Table[i+1] = Table[i]
    else:
      Table[i+1] = Table[0]
    print(Table)
#job(Table,snum)

import os
os.system("clear")


def add(num1,num2):
  return num1+num2
def remove_element(list1, element):
  return [item for item in list1 if item != element]