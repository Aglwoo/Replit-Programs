import pygame
import random
import charecter

pygame.init()
win = pygame.display.set_mode((400,400))
#hitbox
tim = True


#def drawcharecter():

#charecter
ox = 100
oy = 400
ox1 = 200
oy1 = 390
ox2 = 300
oy2 = 370
holex = 177.5
holew = 45
col = 100
holex=150
holey=330
holex1= 250
holey1= 330
left = True
right = False
xe = 360
ye = 330
hit = False
bx = 250
by = 295
bx1 = 310
by1 = 275
bx2 = 360
by2 = 320
bx3 = 465
by3 = 300
bw = 15
bh = 10
x = 50
y = 300
width = 20
height = 65
#enemy
ycheck = 320
ycheck1 = 300
x1 = 50
y1 = 300
width1 = 20
height1 = 30
x2 = 50
y2 = 300
level = 1
width2 = 40
height2 = 60
heightcheck = 60
vel = 2
velcheck = 2
isJump = False
jumpCount = 8
speed = 3
count = 1

run = True
coinx = 260
coiny = 190
coinx1 = 220
coiny1 = 190
coinx2 = 180
coiny2 = 190
coincount = 0
hitx2 = 170
hity2 = 180
hitx1 = 210
hity1 = 180
hitx = 250
hity =180
width3 = 40
height3 = 80
x3 = 50
y3 = 300
pygame.display.set_caption("Level of doom")
print("Made by J and Darth A")
print("Made by J and Darth A")
print("Made by J and Darth A")
while run == True:

    pygame.time.delay(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
      
#left  
    if keys[pygame.K_LEFT] and x > vel or keys[pygame.K_a] and x > vel :
        height = heightcheck
        x -= vel
        pygame.display.update() 
#right
    if keys[pygame.K_RIGHT] and x < 400 - vel - width or keys[pygame.K_d] and x < 400 - vel - width:
        height = heightcheck
        x += vel
        pygame.display.update() 
#jump        
    if not(isJump):
#jumping
        if keys[pygame.K_SPACE] and y < 380 - height - vel or keys[pygame.K_w] and y < 380 - height - vel or keys[pygame.K_UP] and y < 380 - height - vel:
          height = heightcheck
          isJump = True
          pygame.display.update() 
# crouch                                          
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 70
            pygame.display.update()
            y = ycheck1
            pygame.display.update()
        else:
          height = 40
          y = ycheck
          pygame.display.update()
#sprinting
        if not(keys[pygame.K_LSHIFT]):
          vel = velcheck
          pygame.display.update()
        
        else:
          if not(keys[pygame.K_SPACE]) or not(keys[pygame.K_UP]) or not(keys[pygame.K_w]) and keys[pygame.K_LSHIFT]:
            vel = 6
            
            pygame.display.update()
    
    else:
      if jumpCount >= -8:
        y -= (jumpCount * abs(jumpCount)) * 0.5
        jumpCount -= 1
        pygame.display.update()
        
        
      else: 
        jumpCount = 8
        isJump = False
        pygame.display.update()

#background / level 
    if keys[pygame.K_p]:
      level = input("level num")
      level = int (level)
      level = level - 1
      level = level + 1
      x = 50
      y= 300
      ycheck = 300
      ycheck1 = 320
      ycheck = 320
      height= 60
      width = 40
    pygame.display.update() 
    if level == 1:
      ycheck = 320
      ycheck1 = 300
      character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
      win.fill((200,250,250)) 
      pathofdoom = pygame.draw.rect(win,(200,100,55),(20,340,355,45))
#hitbox
      
      charecter.stealthchar(x,y)
      if x >= 340:
        level = 2
        x = x1
        y= y1
        height= height1
        width = width1
        pygame.display.set_caption("level of doom")
#stairs   
    if level == 2:
      character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
      win.fill((0,0,200)) 
      pathofdoom = pygame.draw.polygon(win,(200,100,55),((20,340), (400, 340), (400, 50), (360, 50), (360, 90), (320, 90), (320, 130), (280, 130), (280, 170), (240, 170),(240, 210), (200, 210),(120, 300), (80, 300), (80, 340) ))
      charecter.stealthchar(x,y) 
      if x > 80 :
        ycheck = 260
        ycheck1 = 240
        pygame.display.update()
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 60
            pygame.display.update()
            y = ycheck1
        else:
          height = 40
          y = ycheck
          pygame.display.update()
      if x >= 120 :
        ycheck = 220
        ycheck1 = 200
        pygame.display.update()
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 60
            pygame.display.update()
            y = ycheck1
            pygame.display.update()
        
      if x >= 160 :
         ycheck = 180
         ycheck1 = 160
         pygame.display.update()
      if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 60
            pygame.display.update()
            y = ycheck1
            pygame.display.update()
      else:
            height = 40
            y = ycheck
            pygame.display.update()
      if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
          height = 60
          pygame.display.update()
          y = ycheck1 
          pygame.display.update()           
        
      if x >= 210 :
        ycheck = 135
        ycheck1 = 115
        pygame.display.update()
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 60            
            y = ycheck1
            pygame.display.update()
        else:
          height = 40
          y = ycheck
          pygame.display.update()
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
            height = 60
            pygame.display.update()
            y = ycheck1
        
      if x >= 250 :
        ycheck = 95
        ycheck1 = 75
        pygame.display.update()
      if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
        height = 60          
        y = ycheck1
        pygame.display.update()
        
      if x >= 285 :
        ycheck = 65
        ycheck1 = 45
        pygame.display.update()
        if not(keys[pygame.K_c]) and not(keys[pygame.K_DOWN]) and not(keys[pygame.K_s]):
          height = 60
          pygame.display.update()
          y = ycheck1
          pygame.display.update()
        
      if x >= 320 :
        ycheck = 20
        ycheck1 = 1
        pygame.display.update()

      if x >= 350:
        level = 3
        x = x2
        y= y2
        ycheck = y2
        ycheck1 = y2
        height= height2
        width = width2
        pygame.display.set_caption("level of doom")
       

#third level
    if level == 3:
      ycheck = 320
      ycheck1 = 300
      bx = 250
      by = 300
      bx1 = 300
      by1 = 275
      bx2 = 360
      by2 = 320
      bx3 = 465
      by3 = 300
      character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
      win.fill((100,200,190)) 
      pygame.display.update
      path = pygame.draw.rect(win,(0,100,55),(20,340,355,45))
      charecter.stealthchar(x,y)
      ehit = pygame.draw.rect(win,(100,200,190),((xe - 20,ye - 20,40,30)))
      charecter.enemy(xe,ye)
      if left == True:
        xe = xe - 4
        if xe <= 20:
          left = False
          right = True
      if right == True:
        xe = xe + 4
        if xe >= 390:
          left = True
          right = False
      if character.colliderect(ehit):
        level = 1
        xe = 390


      
      


      
      
      def spawncoin():
        pygame.draw.circle(win, (250, 250, 0), ((coinx ,coiny)), 10)
      coinbox2 = pygame.draw.rect(win,(100,200,190),(hitx,hity,20,20))
      spawncoin()
      if character.colliderect(coinbox2):
        coincount = coincount + 1
        print("You have",coincount,"coin")
        coinx = -10
        coiny = -10
        hitx = -10
        hity = -10
        pygame.display.update 

      def spawncoin1():
        pygame.draw.circle(win, (250, 250, 0), ((coinx1 ,coiny1)), 10)
      coinbox1 = pygame.draw.rect(win,(100,200,190),(hitx1,hity1,20,20))
      spawncoin1()
      if character.colliderect(coinbox1):
        coincount = coincount + 1
        print("You have",coincount,"coin")
        coinx1 = -10
        coiny1 = -10
        hitx1 = -10
        hity1 = -10
        pygame.display.update 

      def spawncoin2():
        pygame.draw.circle(win, (250, 250, 0), ((coinx2 ,coiny2)), 10)
      coinbox = pygame.draw.rect(win,(100,200,190),(hitx2,hity2,20,20))
      spawncoin2()
      if character.colliderect(coinbox):
        coincount = coincount + 1
        print("You have",coincount,"coin")
        coinx2 = -10
        coiny2 = -10
        hitx2 = -10
        hity2 = -10
        pygame.display.update 
#fourth level
      if x >= 350:
        level = 4
        x = x3
        y= y3
        ycheck = y3
        ycheck1 = y3
        height= height3
        width = width3
        pygame.display.set_caption("Is this blood")
        pygame.display.update
        character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
        

    if level == 4:
      ycheck = 320
      ycheck1 = 300
      character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
      pygame.display.update     
      win.fill((200,20,70)) 
      path = pygame.draw.rect(win,(0,100,55),(20,340,355,45))
      charecter.stealthchar(x,y)

      bullet = pygame.draw.rect(win,(0,255,0),(bx,by,bw,bh))
      bullet1 = pygame.draw.rect(win,(255,255,0),(bx1,by1,bw,bh))
      bullet2 = pygame.draw.rect(win,(255,100,180),(bx2,by2,bw,bh))
      pygame.time.delay(10)
      bullet3 = pygame.draw.rect(win,(255,255,255),(bx3,by3,bw,bh))

      if character.colliderect(bullet):
        level = 1
        x = 20
        xe = 380
      if character.colliderect(bullet1):
        level = 1
        x = 20
        xe = 380
      if character.colliderect(bullet2):
        level = 1
        x = 20
        xe = 380
      if character.colliderect(bullet3):
        level = 1
        x = 20
        xe = 380

      ranumy = random.randint(350,388)
      ranumx = random.randint(20,388)
      ranumy1 = random.randint(350,388)
      ranumx1= random.randint(20,388)
      ranumy2 = random.randint(350,388)
      ranumx2 = random.randint(20,388)
      ranumy3 = random.randint(350,388)
      ranumx3 = random.randint(20,388)
      ranumy4 = random.randint(350,388)
      ranumx4 = random.randint(20,388)
      ranumy5 = random.randint(350,388)
      ranumx5 = random.randint(20,388)
      bx = bx - 4
      bx1 = bx1 - 3
      bx2 = bx2 - 2
      bx3 = bx3 - 2
      if bx3 <= 1:
        
        pygame.draw.line(win,(0,50,0),[ranumx, ranumy ],[ranumx1,ranumy1],5)
        pygame.time.delay(1)
        pygame.draw.line(win,(0,50,0),[ranumx2, ranumy2 ],[ranumx3,ranumy3],5)
        pygame.time.delay(1)
        pygame.draw.line(win,(0,50,0),[ranumx4, ranumy4 ],[ranumx5,ranumy5],5)
        pygame.time.delay(1)
        hole = pygame.draw.rect(win,(200,20,70),(holex,340,holew,50))
        holex = holex - 2
        holew = holew + 5.3
        if character.colliderect(hole):
          level = 5
          pygame.display.set_caption("YESSSS finally the only good level. Mini game am i right. EPIC GAMES")
    if level == 5:
      
      ycheck = 100
      ycheck1 = 80
      character = pygame.draw.rect(win,(100,250,250),(x,y-10,width,height))
      pygame.display.update     
      win.fill((100,40,0)) 
      earth = pygame.draw.rect(win,(50,20,0),(0,0,70,400))
      earth1 = pygame.draw.rect(win,(50,20,0),(330,0,70,400))
      
      charecter.stealthchar(x,y)
      isJump = False
      if character.colliderect(earth):
        x = x + 10
        pygame.display.update()
      if character.colliderect(earth1):
        x = x-7
      obstacle = pygame.draw.rect(win,(0,0,0),(ox,oy,20,20))
      obstacle1 = pygame.draw.rect(win,(0,0,0),(ox1,oy1,20,20))
      obstacle2 = pygame.draw.rect(win,(0,0,0),(ox2,oy2,20,20)) 
      oy = oy - 4
      oy1 = oy1 - 5
      oy2 = oy2 - 2
      if character.colliderect(obstacle):
        level = 1
        oy = 400
      if character.colliderect(obstacle1):
        level = 1
        oy1 = 390
      if character.colliderect(obstacle2):
        level = 1
        oy2 = 370

    if level == 6:
      ycheck = 320
      ycheck1 = 300
      character = pygame.draw.rect(win,(0,250,250),(x-10,y-10,width,height))
      pygame.display.update     
      win.fill((240,0,255)) 
      path = pygame.draw.rect(win,(0,250,255),(20,340,355,45))
      charecter.stealthchar(x,y)

   
keys = pygame.key.get_pressed()
