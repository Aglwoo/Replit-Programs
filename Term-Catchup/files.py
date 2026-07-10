import sys
"""
Write a function that takes a telNum as a string and returns True if the number has a len of 11 and contains only digits
Write a function that asks the user to input a tel num and use the function created in part a to check if this number is valid. If the number is valid write the number to a text file called telnums.txt
Create a function that takes a tel number and a the name of country as params and returns the tel number with the correct dialing code attached. E.g. 07723454323 --> +4407723454323 or 13910998888 --> +861391099888
Possible extension: ISBN check digit function or credit card valid
"""
def numcheck():
  number = input("Ur number:")
  if len(number)==11:
    number=int(number)
    print("True")
    
def telnum():
  global num
  num = input("Ur number:")
  if len(num)==11:
    num=int(num)
    print("True")
    file = open("telnums.txt","a")
    file.write(str(num))
    file.write("\n")
    file.close()
  else:
    print("ReRunCodeWithCOrrectInput")
    sys.exit()
    

def full():
  telnum()
  print(num)
  country = input("country (capital first letter please :) : ")
  file = open("telecodes.txt","r")
  for i in range(195):
    #print(file.readline(i))
    line = file.readline(i)
    filecountry = line.split(",")
    #print(str(filecountry[0]))
    if country == str(filecountry[0]):
      fullnum = str(filecountry[1])+str(num)
      print(fullnum)