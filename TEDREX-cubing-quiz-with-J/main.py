score = 0


print("Greetings annd Welcome to the Cubing Quiz")


print("Instructions to the quiz: You will be asked 10 questions, you should just type your answers next to the question. At the end you will get your score.")


demo = input("2+2")
if demo == "4":
  print("correct")
  score = score+1
  print(score)




question1 = input("what year was the rubik's cube invented? ")
if question1 == "1974":
  print("correct")
  score = score+1

question2 = input("True or False: the pyraminx was an alteration of the rubik's cube ")
if question2.lower() == "false":
  print("correct") 
  score = score+1

question3 = input("What are the small piece of a rubik's cube called? ")
if question3.lower() == "cubies":
  print("correct")
  score = score+1

question4 = input("How many combinations of the rubik's cube are there")


if question4 == "43 252 003 274 489 856 000":
  print("correct")
  score = score+1


question5 = input("What year was the first ever rubik's cube competition held in? ")
if question5 == "1982":
  print("correct")
  score = score+1

  
question6 = input("To the nearest whole second, what was the first ever official 3x3 Rubik's cube world record? ")
if question6 == "23":
  print("correct")
  score = score+1


question7 = input("What is the official name of the 5x5x5 rubik's cube? ")
if question7.lower() == "rubik's revenge":
  print("correct")
  score = score+1

  
question8 = input("What 3 dimensional shape is the Megaminx? ")
if question8.lower() == "dodecahedron":
  print("correct")
  score = score+1

  
question9 = input("What number is known as God's Number? ")
if question9 == "20":
  print("correct")
  score = score+1

  
question10 = input("How many events are in the WCA? ")
if question10 == "17":
  print("Correct")
  score = score+1
print("your score was")
print(score)

print('''Thank you for completeing the tedrex / j quiz. Please subscribe to both of them on youtube. 
Tedrex - https://www.youtube.com/channel/UCgR-VSC_UR8ctjwXd5Ed0ug?sub_confirmation=1
j - https://www.youtube.com/channel/UCh9BqvJh-r0ScpGVR4qfkFg?sub_confirmation=1''')