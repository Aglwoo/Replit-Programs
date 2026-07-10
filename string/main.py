name = input("name ")
#usym = input("symbol please")
#usym1 = input("2nd symbol please")
lname = len(name)
#print(usym*lname)
#print(name.upper())
#print(usym*lname)
#print("")

#if (lname % 2) == 0:
#  print()
#  lname = lname/2
#  lname= int(lname)
 # print((usym+usym1)*lname)
  #print(name)
  #print((usym+usym1)*lname)
#else:
#  lname = lname = lname/2
#  lname = lname-0.5
#  lname= int(lname)
#  print((usym+usym1)*lname + usym)
#  print(name)
#  print((usym+usym1)*lname + usym)

lname = 23 - lname
lname = lname/2
lname = int(lname) -1
space = " "
if (lname % 2) == 0:
  print("         \\|||||/        ")
  print("         ( O O )         ")
  print("|--ooO-----(_)----------|")
  print("|                       |")
  print("|"+space*lname,name, space*lname+" |")
  print("|                       |")
  print("|------------------Ooo--|")
  print("         |__||__|        ")
  print("          ||  ||         ")
  print("         ooO  Ooo        ")
else:
  print("         \\|||||/        ")
  print("         ( O O )         ")
  print("|--ooO-----(_)----------|")
  print("|                       |")
  print("|"+space*lname,name, space*lname+"|")
  print("|                       |")
  print("|------------------Ooo--|")
  print("         |__||__|        ")
  print("          ||  ||         ")
  print("         ooO  Ooo        ")