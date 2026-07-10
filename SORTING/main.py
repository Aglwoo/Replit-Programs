def bubblesort():
  mylist = []
  cycle = True
  numnums = 0
  while cycle == True:
    firstnum = input("num1 ")
    if firstnum == "end":
      print("end")
      cycle = False
    else:
      mylist.append(int(firstnum))
      numnums = numnums+1
      print(mylist)
    print(cycle)
  print(mylist)

  end = False
  num1=0
  num2=1
  while end != True:
    if mylist[num1] > mylist[num2]:
      block1 = mylist[num1]
      block2 = mylist[num2]
      mylist[num1] = block2
      mylist[num2] = block1
      print(mylist)
      
    else:
      if num1 < numnums-1:
        num1 = num1+1
      if num2 < numnums-1:
            num2 = num2+1
      else:
        num1 = 0
        num2 = 1
        



def linearsearch(unsorted_list,elem):
  len_list=len(unsorted_list)
  found=0

  for i in range(len_list):
    if unsorted_list[i] == elem:
      found = 1
      break
    return found

elem = -1
unsorted_list = [4,5,6,7,8,9]
#linearsearch(linearsearch(unsorted_list,elem))


