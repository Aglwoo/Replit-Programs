import time
import os
import random
def one():
  print("""
  _____________
  |           |
  |           |
  |     .     |
  |           |
  |___________|""")

def two():
  print("""
  _____________
  |           |
  |        .  |
  |           |
  |  .        |
  |___________|""")

def three():
  print("""
  _____________
  |           |
  |        .  |
  |     .     |
  |  .        |
  |___________|""")

def four():
  print("""
  _____________
  |           |
  |  .     .  |
  |           |
  |  .     .  |
  |___________|""")
def five():
  print("""
  _____________
  |           |
  |  .     .  |
  |     .     |
  |  .     .  |
  |___________|""")

def six():
  print("""
  _____________
  |           |
  |  .     .  |
  |  .     .  |
  |  .     .  |
  |___________|""")



def rolling():
  os.system("clear")
  six()
  print("Rolling.")
  time.sleep(0.3)
  os.system("clear")
  three()
  print("Rolling..")
  time.sleep(0.3)
  os.system("clear")
  one()  
  print("Rolling...")
  time.sleep(0.3)
  os.system("clear")
  four()
  print("Rolling.")
  time.sleep(0.3)
  os.system("clear")



def dicerolled(i,point1,bob):
  rolling()  
  roll = random.randint(1,6)
  if roll%2 == 0:
    if roll == 2:
      two()
    if roll == 4:
      four()
    if roll == 6:
      six()
    point1 = point1+10
    print(roll,"- even number","points: ",point1)
    time.sleep(2)
  elif roll % 2 !=0:
    if roll == 1:
      one()
    if roll == 3:
      three()
    if roll == 5:
      five()
    point1 = point1 - 5
    if point1 <=0:
      point1 = 0
    print(roll,"- odd number,","points: ",point1)
    time.sleep(2)
    print("\n")

  roll2 = random.randint(1,6)
  if roll2%2 == 0:
    if roll2 == 2:
      two()
    if roll2 == 4:
      four()
    if roll2 == 6:
      six()
    point1 = point1 +10
    print(roll2,": even number","points: ",point1)
    time.sleep(2)
  else:
    if roll2 == 1:
      one()
    if roll2 == 3:
      three()
    if roll2 == 5:
      five()
    point1 = point1 - 5
    if point1 <=0:
      point1 = 0
    print(roll2,"- odd number,","points: ",point1)
    time.sleep(2)
    print("\n")
  if roll == roll2:
    print("double")
    bob = bob+1
  return bob
  return point1
