#counts number of lines in the file
def linecount():
  file1 = open("data.txt", 'r')
  for i, line in enumerate(file1):
    pass
  print('Total Lines', i + 1)
  filelen = i
  return filelen
#variable storing number of lines in the dile
filelen = int(linecount()+1)

height =input("How tall are you? (in Cm)")
weight = input("How much do you weight? (in Kg)")
overweight = input("Are you overweight/underweight/normal")
print("Thanks")
person = [height,weight,overweight]
print(person)
with open("data.txt", 'r') as file:
  list = file.readlines()
  for i in range(filelen):
    print(list[i])



