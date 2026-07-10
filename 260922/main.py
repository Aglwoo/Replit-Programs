#age = input("age")
#age = int(age)
def q2(age):
  if age >= 13 and age<=19:
    print("TEEENAGERRERER")
    if age == 15:
      print("ur 15 - thats my age")
  elif age> 50 and age<130:
    print("OLDDddddd")
  elif age > 130:
    print("OLDDDDD")
  else:
    print("OK cool")


#mile = input("millage")
#age  = input("age")
def car(mile, age):
  if age< 0 or mile<0:
    print("FAKE")
  elif age<= 5 and miles < 10000:
    print("TRUEEE")
  else:
    print("FAKE FAKE FAKE FAKE FAKE FAKE FAKE FAKE FAKE FAKE FAKE FKAE FKAEF EKFAEF")

















word = "incredible"
#letter1=input("input a charecter or number")
#letter2=input("input another charecter or number")
def lettercheck(letter1,letter2):
  if letter1 in word and letter2 in word:
    print("both in word")
  elif letter1 in word:
    print(letter1, "in", word)
  elif letter2 in word:
    print(letter2, "in", word)     
  else:
    print("not in word")


