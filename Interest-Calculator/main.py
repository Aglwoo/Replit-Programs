print("A house is set at a value of £100 000")
house = 100000
intrest = input("What percentge of the price would you like it to go up by every year")
intrest = int(intrest)
year = 1
fin = input("What price do you want the house to be eventually")
fin=int(fin)
while fin>house:
  print("Your price on year",year,"is",intrest+intrest/100)
  year = year+1
print("The end")
