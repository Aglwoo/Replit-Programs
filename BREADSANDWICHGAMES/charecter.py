import pygame
pygame.init()
win = pygame.display.set_mode((400,400))
def stealthchar(x,y,left):
  if left != True:
  #new hit box
  #pygame.draw.
  #face
    pygame.draw.circle(win, (0, 0, 0), ((x ,y)), 10)
  #robe 
    pygame.draw.polygon(win,(60, 60, 60), ((x, y+5),(x+10,y+50),(x-10,y+50)))
  #face mask
    pygame.draw.polygon(win,(80,80,80), ((x-2,y-2), (x+2,y-2),(x+2,y-6),(x+6,y-6),(x+6,y-10),(x+10,y-10),(x+10,y-14),(x-6,y-14),(x-6,y-10),(x-10,y-10),(x-10,y-6),(x-14,y-6),(x-14,y+2),(x-10,y+2),(x-10,y+6),(x-6,y+6),(x-6,y+10),(x+2,y+10)))
  #eyes
    pygame.draw.rect(win,(255,0,0),((x + 2,y,3,3)))
    pygame.draw.rect(win,(255,0,0),((x + 7,y,3,3)))
  else:
    leftstealthchar(x,y)
  

def leftstealthchar(x,y):
  #face
  pygame.draw.circle(win, (0, 0, 0), ((x ,y)), 10)
  #robe 
  pygame.draw.polygon(win,(60, 60, 60), ((x, y+5),(x+10,y+50),(x-10,y+50)))
  #face mask
  pygame.draw.polygon(win,(80,80,80), ((x+2,y+2), (x-2,y+2),(x-2,y+6),(x-6,y+6),(x-6,y+10),(x-10,y+10),(x-10,y+14),(x+6,y+14),(x+6,y+10),(x+10,y+10),(x+10,y+6),(x+14,y+6),(x+14,y-2),(x+10,y-2),(x+10,y-6),(x+6,y-6),(x+6,y-10),(x-2,y-10)))
  pygame.draw.polygon(win,(80,80,80), ((x+2,y-2), (x-2,y-2),(x-2,y-6),(x-6,y-6),(x-6,y-10),(x-10,y-10),(x-10,y-14),(x+6,y-14),(x+6,y-10),(x+10,y-10),(x+10,y-6),(x+14,y-6),(x+14,y+2),(x+10,y+2),(x+10,y+6),(x+6,y+6),(x+6,y+10),(x-2,y+10)))
  #eyes
  pygame.draw.rect(win,(255,0,0),((x - 2,y,3,3)))
  pygame.draw.rect(win,(255,0,0),((x - 7,y,3,3)))
    



#arji character
def supportchar(x,y):
  pygame.draw.circle(win,(255,100,10),((x - 35,y + 10)),15)
  pygame.draw.rect(win,(255,255,0),((x-40,y + 5,3,3)))
  pygame.draw.rect(win,(255,255,0),((x-30,y + 5,3,3)))

#arjienemy
def enemy(xe,ye):

  pygame.draw.circle(win,(255,100,10),((xe,ye)),20)
  pygame.draw.rect(win,(0,0,0),((xe - 5,ye - 3,4,4)))
  pygame.draw.rect(win,(0,0,0),((xe + 3,ye - 3,4,4)))
  pygame.draw.rect(win,(0,0,0),((xe - 4,ye + 4,10,3)))
  pygame.draw.rect(win,(0,0,0),((xe - 5,ye + 4,2,5)))
  pygame.draw.rect(win,(0,0,0),((xe + 4,ye + 4,2,5)))
  pygame.draw.rect(win,(0,0,0),((xe - 7,ye + 6,2,5)))
  pygame.draw.rect(win,(0,0,0),((xe + 6,ye + 6,2,5)))

  


  
  