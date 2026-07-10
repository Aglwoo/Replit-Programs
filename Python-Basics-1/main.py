import random
score =  0
restart = True
print("Hi welcome to my code. This is a maths quiz ")

while restart == True:
  
  func = random.randint(1,3)
  randomnum = random.randint(1,100)
  randomnum2 = random.randint(1,100)
  randomnum = str(randomnum)
  randomnum2 = str(randomnum2)


  if func == 1:
    print("multiplying")
    subans = input(randomnum+"x"+randomnum2+" ")
    if int(subans) == int(randomnum) * int(randomnum2):
      print("correct")
      score = score+1


  if func == 2:
    print("add")
    addans = input(randomnum+"+"+randomnum2+" ")
    if int(addans) == int(randomnum) + int(randomnum2):
      print("correct")
      score = score+1

  if func == 3:
    print("subtract")
    subans = input(randomnum+"-"+randomnum2+" ")
    if int(subans) == int(randomnum) - int(randomnum2):
      print("correct")
      score = score+1
  


