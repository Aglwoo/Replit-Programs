import bob

groups=["blue","green","green","red","red","green","blue","blue","green","green","red","red","green","blue","green","green"]
blue = 0
red= 0
green =0
for i in range(len(groups)):
  if groups[i] == "blue":
    blue = blue +1
    print(blue)
  if groups[i] == "green":
    green = green +1
    print(green)
  if groups[i] == "red":
    red = red +1
    print(red)

  if groups[i] == "blue":
    blue = blue +1
    print(blue)
  if groups[i] == "green":
    green = green +1
    print(green)
  if groups[i] == "red":
    red = red +1
    print(red)

months=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]


studentnames = ["Rob", "Anna", "Huw", "Emma", "Patrice", "Iqbal"]
for i in range(len(studentnames)):
  print("bob")


file = open("bob.py", "w")
file.writelines("""def bob():
  bob = "timmy"
  print(bob)""")
file.close()
bob.bob()