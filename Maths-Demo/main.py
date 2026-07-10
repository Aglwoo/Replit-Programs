#### BASIC IDEA ####
#if else, while loop, maths calculations and symbols
### FOR EPISODE ####
run = True
randomnum = 1

while run == True:
  if randomnum <= 5:
    print(randomnum)
    randomnum = randomnum+1

  elif randomnum <= 10 and randomnum> 5:
    print("More than 5 and less than 11")
    randomnum = randomnum+1


  else:
    print("bigger than 11")
    quit()