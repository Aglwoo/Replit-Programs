import random
import time
jimmy = []
while True:
  l1 = random.randint(1,5)
  l2 = random.randint(1,5)
  l3 = random.randint(1,5)

  if l1 == 1:
    l1 = 'a'
  if l1 == 2:
    l1 = 'g'
  if l1 == 3:
    l1 = 'l'
  if l1 == 4:
    l1 = 'w'
  if l1 == 5:
    l1 = 'o'

  if l2 == 1:
    l2 = 'a'
  if l2 == 2:
    l2 = 'g'
  if l2 == 3:
    l2 = 'l'
  if l2 == 4:
    l2 = 'w'
  if l2 == 5:
    l2 = 'o'

  if l3 == 1:
    l3 = 'a'
  if l3 == 2:
    l3 = 'g'
  if l3 == 3:
    l3 = 'l'
  if l3 == 4:
    l3 = 'w'
  if l3 == 5:
    l3 = 'o'
  row = [l1,l2,l3, ' ']
  with open('jimmy','a') as jimmy:
    jimmy.writelines(row)
  time.sleep(0.3)