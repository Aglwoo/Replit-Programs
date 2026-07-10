def task1():
    scores = [[22,32,11,45],[13,56,12,44],[24,55,77,88]]
    print(scores)
    print("b")
    print(scores[0])
    print("c")
    finalnum = len(scores[0])
    print(scores[0][0], scores[0][finalnum-1])
    print("d")
    for i in range(len(scores)):
      for j in range(len(scores[i])):
        print(scores[i][j])
    print("e")
    for i in range(len(scores)):
      for j in range(len(scores[i])):
        print("student",i,"scored",scores[i][j])
    print("f")
    for i in range(len(scores)):
      print("Student",i,"scored:")
      for j in range(len(scores[i])):
        print(scores[i][j],"in test",j)
    print("g")
    total = 0
    for i in range(len(scores)):
      for j in range(len(scores[i])):
        total += scores[i][j]
    print(total)
    number=0
    print("h")
    for i in range(len(scores)):
      for j in range(len(scores[i])):
        number = number+1
    average = total/number
    print(average)
    print("i")

    for i in range(len(scores)):
      total2=0
      number=0
      for j in range(len(scores[i])):
        total2 += scores[i][j]
        #print(total2)
        number = number+1
        print(total2/number)
    print("j")
    for i in range(len(scores)):
      high = 0
      num2 = 0
      for j in range(len(scores[i])):
        num = scores[i][j]
        if num > high:
          high=num
      print(high)

    #data set 2
    scores2 = [["Malcom",22,32,11,45,18,29,76],["Greg",13,56,12,44,56],["Helen",24,55,77,88,85,66,72,93]]
    for i in range(len(scores2)):
      high = 0
      for j in range(1,len(scores2[i])):
        if scores2[i][j] > 50:
          high += 1
      print("highest:",high)
    #data set 3
    scores3 = [["Malcom",22,32,"Absent",11,45,18,29,76,"Absent"],["Greg","Music lesson",13,56,12,"Absent",44,56],["Helen",24,55,77,88,85,66,72,93,70]]
    for i in range(len(scores3)):
      total3=0
      numb=0
      for j in range(1,len(scores3[i])):
        if str(scores3[i][j]).isdigit() == False:
          total3 += 1
          print("digit")
        else:
          numb+=1
          total3 += 1
      print(numb,"/",total3)
    
          