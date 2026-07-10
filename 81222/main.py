scores3 = [["Malcom",22,32,"Absent",11,45,18,29,76,"Absent"],["Greg","Music lesson",13,56,12,"Absent",44,56],["Helen",24,55,77,88,85,66,72,93,70]]

# Name , score

#Output the number of tests taken by each student as a ratio. Malcom sat 7/9 tests.

def pick(scores3):
  sl = len(scores3)
  attendance = 0
  for i in range(sl):
    ssl = scores3[i][i+1]
    name = scores3[i][0]
    print(name)
    attendance = 0
    for x in range(i ):
      if type(scores3[i][x+1]):
        attendance = attendance+1
        print(attendance)


    
    


pick(scores3)

    
print(scores3[1][1])
print(type(scores3[1][1]))