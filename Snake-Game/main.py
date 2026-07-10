import random
import sys
import time
snake=1
heal=1
while "1"=="1":
 
  occur=['you have come across an apple','you ate a poisonos apple','you ran into a rock','you can pick up a potion of healing']
  over=['you were picked up by a bird and eaten','you climed up a tree and found 2 apples']
  under=['you found 2 apples under the rock','the rock fell and you got crushed']
  around=['you saw 3 apples on a tree and wished you went over the rock']

  choice=(random.choice(occur))
  occur=choice
  if snake<1:
    print("GAME OVER")
    sys.exit(0)
  print(occur)
  0=="game over. sorry if it happened straight away.I have not yet figured out how to fix it"
  if choice=='you have come across an apple':
    dot=input("Type yes if you want to eat it")
    if dot=="yes":
      snake=snake+1
      print(snake)
  if choice=='you ate a poisonos apple':n
    if heal==0:
      print("Ooof. Too bad. Your snake has now shrunk in size. Sorry if it happened straight away. Dont know how to fix it")
      snake=snake-1
      print (snake)
    if heal>0:
      answer=input("you have a potion of healing do you want to use it? You do not have to. You can conserve them for worse times if you want to.")
      if answer=="yes":
        print("great you just saved your self from losing a life")
        heal=heal-1
      if answer=="no":
        print("that is fine. Your choice.")
        snake=snake-1
        print(snake)


  if choice=='you ran into a rock':
    under=(random.choice(under))
    over=(random.choice(over))
    move=input("chose if you would like to go under the rock, around the rock or over the rock. Just type under, around or over. There is a chance you will get two apples or lose two lives. Choose wisely. I recommend you should check your lives before you try(Very risky). GOING AROUND WILL MEAN NOTHING WILL HAPPEN TO YOU")
    if move=="under":
      if under=='the rock fell and you got crushed':
        print(under,"too bad you have lost two lives")
        snake=snake-2
        print(snake)
      if under=='you found 2 apples under the rock':
        print(under,"lucky you")
        snake=snake+2
        print(snake)
    if move=="over":
      if over=='you were picked up by a bird and eaten':
        print(over, "luckily you escaped. You have bled a lot but lost two lives")
        snake=snake-2
        print(snake)
      if over=='you climed up a tree and found 2 apples':
         print(over, "Well who would have thought!!!!!!")
         snake=snake+2
         print(snake)
    if move=="around":
      print(around)
      print("tut tut")
      print("Now i quote neil armstrong:  There can be no great accomplishment without risk")
      time.sleep(3)
 
  if choice=='you can pick up a potion of healing':
    potion=input("do you want to pick it up?")
    if potion=="yes":
      heal=heal+1
      print("great you now have", heal,"potion/s")
    if potion=="no":
      print("fine that is your choice. You have",heal,"potions")