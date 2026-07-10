import os
import time
blue = ["Mark","Alfie,","Nick","Michael,","Lauren","Fred","Grace","Henry","Greg","Robert","Ruby","Alice","Harry","John","Victor","Ethan","Charlotte","Victoria","Reggie"]

green = ["Vicky","Fredo","Harper","Alison","Scott","David","Sarah","Jenny","Abdul","Mo","Jacob","Jed","Greg","Andy","William","Sarah","Nicky","Mark"]

lblue = len(blue)
lgreen = len(green)
def q1a():

  for i in range(lblue):
    print(blue[i])
  

  for i in range(lgreen):
    print(green[i])

def q1b(lblue,lgreen):
  if len(blue)>len(green):
    print("length of blue is bigger than green by",lblue-lgreen)
  else:
    print("length of green is longer than blue by",lgreen-lblue)

def q2():
  run = True
  list = ["bob","zim","test","tod"]
  while run == True:
    inc = 0
    p = "0"
    
    llist = len(list)
    choice = input("""_____MENU_____
1. View list
2. Search for a name in the list
3. Add a name to the list
4. Remove a name from the list
5 Sort the list
0. Quit program""")
    print("")
    if choice == "1":
      if list == []:
        print("empty list")
      else:
        for i in range(llist):
          print(list[i])
    elif choice == "2":
      search = input("""1. search by name
2. search by usernumber""")
      if search == "1":
        sname = input("what name do you want to look for?")
        for i in list:
          inc = inc+1
          if i == sname:
            p = 1
            break
        if p == 1:
          print(sname,"is present in position",inc)
        else:
          print("Name is not present")
      if search == "2":
        unum = input("what usernumber do you want to look for?")
        unum = int(unum)-1
        if len(list)>unum:
          print(list[unum])
        else:
          print("not in list")
    elif choice == "3":
      na = input("what name do you want to add")
      where = input("""1. Add to the end
2. add to the start
3. add to the middle""")
      if where == "1":
        list.append(na)
        print(list)

      if where == "2":
        list = [na,*list]
        print(list)

      if where == "3":
        half = len(list)//2
        list.insert(half, na)
        print(list)
    elif choice == "4":
      remwhich = input("""1. remove by name
2. remove by user number""")
      llist = len(list)
      if remwhich == "1":
        rname = input("Name you want to remove?")
        for i in range(llist):
          if list[i] == rname:
            list[i] = "*Deleted*"
            print("done")
      if remwhich == "2":
        numr = input("which position needs to be deleted?")
        numr = int(numr)-1
        list[numr] = "*Deleted*"
        print("done")
      
    elif choice == "5":
      order= input("""1. alphabetical
2. flipped list""")
      if order == "1":
        orderlist = list
        orderlist.sort(reverse=False)
        print(orderlist)
      if order == "2":
        orderlist = list
        orderlist.sort(reverse=True)
        print(orderlist)

    time.sleep(5)
    os.system('clear')


q2()
