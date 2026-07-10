import random 


def q1():
  word = input("Word: ")
  num = input("Times ")
  num = int(num)
  for i in range(num):
    print(word)

def q2():
  tnum = input("times ")
  tnum = int(tnum)
  for i in range(12):
    print((i+1)*tnum)

def q3():
  word = input("Word ")
  lword= len(word)
  for i in range(lword):
    print(word[i])
def q4():
  word =input("WOrd: ")
  amount = 0
  letter = input("1 letter: ")
  for i in range (len(word)):
    if word[i] == letter:
      amount = amount +1
  print(amount,"times that",letter,"apears")
 
  

def q5():
  