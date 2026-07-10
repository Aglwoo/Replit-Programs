import os
import time

height1 =True



def linecount():
  file1 = open("data.txt", 'r')
  for i, line in enumerate(file1):
    pass
  print('Total Lines', i + 1)
  filelen = i
  return filelen
bob = True
while True:
  Run = int(input("""1: Data intake 
2: Data Comparison
"""))
  #Data comparison
  while Run == 2:
    filelen = int(linecount()+1)
    with open("data.txt", 'r') as file:
      list = file.readlines()
      for i in range(filelen):
        commacheck = list[i]
        height1 =True
        for x in range(len(commacheck)):
          print(commacheck[x])
          if commacheck[x] == "," and height1 == True:
            print("Comma detected")
            height2 = commacheck[0:x]
            print(height2)
            print("Ending Code")
            time.sleep(2)
            height1 = False
            weight1 = True
            print(weight1)
            break
          elif commacheck[x] == "," and weight1 == True:
            print("Second comma detected")
            time.sleep(2)
            break
          print("bob is fat")
          time.sleep(2)
        os.system("clear")
    commacheck = list
  #Data intake
  while Run == 1:
    #variable storing number of lines in the dile
    filelen = int(linecount()+1)
    
    height =input("How tall are you? (in Cm)   ")
    weight = input("How much do you weight? (in Kg)   ")
    overweight = input("Are you (1)overweight/(2)underweight/(3)normal?   ")
    if overweight == "1" or overweight == "2" or overweight == "3":
      print("Thanks")
      time.sleep(5)
      os.system("clear")
      Run = 0
      
    
    
      person = [height,weight,overweight]
      
      with open("data.txt", 'r') as file:
        list = file.readlines()
        for i in range(filelen):
          print(list[i])
          time.sleep(2)
          os.system("clear")
      
      
      with open("data.txt", "a") as write:
        write.writelines(height)
        write.writelines(",")
        write.writelines(weight)
        write.writelines(",")
        write.writelines(overweight)
        write.writelines("\n")
    
    else:
      print("Invalid Restarting Code")
      time.sleep(5)
      os.system("clear")
      Run = 0





