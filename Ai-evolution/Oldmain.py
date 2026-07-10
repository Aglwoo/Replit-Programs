import random
import os
import time
import math

#vaiables
age = 0
hunger=0
thirst=0
speed=1
stamina=50
maxage=10
generation=1
score=0
maxx=10
maxy = 10
x=5
ox=5
y=5
oy=5
tic=0
oc=0
fx=10
fy=10
#actions
#look for food - always top right 5,5
#move to water in a set location
#create a home (set of coords) to sleep at night and has to sleep in that location after first night every three days or dies

########CODE########
def spawn(x,y):
  dotx=x
  doty=y

def movel():
  global x, ox
  ox=x
  x=x-1
  print(x,y,"left")
def mover():
  global x, ox
  ox=x
  x=x+1
  print(x,y,"right")
def moveu():
  global y,oy
  oy=y
  y=y+1
  print(x,y,"up")
def moved():
  global y,oy
  oy=y
  y=y-1
  print(x,y,"down")

def choosemove(x,y):
  global choice
  choice=random.randint(1,4)
  if choice==1:
    movel()
    choice="left"
  if choice==2:
    mover()
    choice="right"
  if choice==3:
    moveu()
    choice="up"
  if choice==4:
    moved()
    choice="down"
def gmove():
  global fx,fy,score
  if fx-x<fx-ox or fy-y<fy-oy:
    score=score+1
    print(score)
    with open('storemove.txt', 'a') as f:
      data = choice
      f.write(data)
  else:
    score=score-1
    



run=0
while run<10:
  choosemove(x,y)
  gmove()
  run=run+1


print(score)
