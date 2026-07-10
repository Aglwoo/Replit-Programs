def bob():
  bob = "timmy"
  print(bob)
  file1 = open("tim.py","w")
  file1.writelines("""def tim():
    bob = timmy
    print(bob)""")
  file1.close()