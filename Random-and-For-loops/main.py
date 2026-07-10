import random

func = random.randint(1,3)
randomnum = random.randint(1,100)
randomnum2 = random.randint(1,100)
randomnum = str(randomnum)
randomnum2 = str(randomnum2)

print(func)

if func == 1:
  print("multiplying")
  subans = input(randomnum+"x"+randomnum2+" ")
  if int(subans) == int(randomnum) * int(randomnum2):
    print("correct")


if func == 2:
  print("add")
  addans = input(randomnum+"+"+randomnum2+" ")
  if int(addans) == int(randomnum) + int(randomnum2):
    print("correct")

if func == 3:
  print("subtract")
  subans = input(randomnum+"-"+randomnum2+" ")
  if int(subans) == int(randomnum) - int(randomnum2):
    print("correct")



