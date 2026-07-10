import time
import picokeypad as keypad
import random

 

last_states = 0
keypad.init()

KEYS = keypad.get_num_pads()

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 255, 0)
CYAN = (0, 255, 255)
GREEN = (0, 0, 255)
PINK = (255, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
coly = random.randint(0,255)
coly1 = random.randint(0,255)
coly2 = random.randint(0,255)
colors = 'blank'

def get_buttons(states):
    buttons = []
    buttonNo = 0
    
    while states > 0:
        if states % 2 == 1:
            buttons.append(buttonNo)
        
        buttonNo += 1
        states = states // 2
    
    return buttons

def art():
    for btn in range (0,16):
        keypad.illuminate((btn),0,0,0)
    keypad.illuminate((12), 255,0,0)
    keypad.illuminate((13), 0,255,0)
    keypad.illuminate((14), 0,0,255)
    keypad.illuminate((15), 0,0,0)
    keypad.update()
art()
while True:
    states = keypad.get_button_states()
    if states != last_states and states !=0:
        buttons = get_buttons(states)
        print(states,buttons)
        if buttons == [12]:
            colors = 'red'
        if buttons == [13]:
            colors = 'green'
        if buttons == [14]:
            colors = 'blue'
        if buttons == [15]:
            colors = 'blank'
        if colors == 'blank':    
            if buttons == [0]:
                keypad.illuminate((0), 0,0,0)
                keypad.update()
            if buttons == [1]:
                keypad.illuminate((1),0,0,0)
                keypad.update()
            if buttons == [2]:
                keypad.illuminate((2), 0,0,0)
                keypad.update()
            if buttons == [3]:
                keypad.illuminate((3),0,0,0)
                keypad.update()
            if buttons == [4]:
                keypad.illuminate((4), 0,0,0)
                keypad.update()
            if buttons == [5]:
                keypad.illuminate((5), 0,0,0)
                keypad.update()
            if buttons == [6]:
                keypad.illuminate((6), 0,0,0)
                keypad.update()
            if buttons == [7]:
                keypad.illuminate((7), 0,0,0)
                keypad.update()
            if buttons == [8]:
                keypad.illuminate((8), 0,0,0)
                keypad.update()
            if buttons == [9]:
                keypad.illuminate((9), 0,0,0)
                keypad.update()
            if buttons == [10]:
                keypad.illuminate((10), 0,0,0)
                keypad.update()
            if buttons == [11]:
                keypad.illuminate((11), 0,0,0)
                keypad.update()
        if colors == 'red':    
            if buttons == [0]:
                keypad.illuminate((0), 255,0,0)
                keypad.update()
            if buttons == [1]:
                keypad.illuminate((1),255,0,0)
                keypad.update()
            if buttons == [2]:
                keypad.illuminate((2),255,0,0)
                keypad.update()
            if buttons == [3]:
                keypad.illuminate((3),255,0,0)
                keypad.update()
            if buttons == [4]:
                keypad.illuminate((4), 255,0,0)
                keypad.update()
            if buttons == [5]:
                keypad.illuminate((5),255,0,0)
                keypad.update()
            if buttons == [6]:
                keypad.illuminate((6),255,0,0)
                keypad.update()
            if buttons == [7]:
                keypad.illuminate((7), 255,0,0)
                keypad.update()
            if buttons == [8]:
                keypad.illuminate((8),255,0,0)
                keypad.update()
            if buttons == [9]:
                keypad.illuminate((9),255,0,0)
                keypad.update()
            if buttons == [10]:
                keypad.illuminate((10),255,0,0)
                keypad.update()
            if buttons == [11]:
                keypad.illuminate((11), 255,0,0)
                keypad.update()
        if colors == 'green':    
            if buttons == [0]:
                keypad.illuminate((0), 0,255,0)
                keypad.update()
            if buttons == [1]:
                keypad.illuminate((1),0,255,0)
                keypad.update()
            if buttons == [2]:
                keypad.illuminate((2), 0,255,0)
                keypad.update()
            if buttons == [3]:
                keypad.illuminate((3),0,255,0)
                keypad.update()
            if buttons == [4]:
                keypad.illuminate((4), 0,255,0)
                keypad.update()
            if buttons == [5]:
                keypad.illuminate((5), 0,255,0)
                keypad.update()
            if buttons == [6]:
                keypad.illuminate((6), 0,255,0)
                keypad.update()
            if buttons == [7]:
                keypad.illuminate((7), 0,255,0)
                keypad.update()
            if buttons == [8]:
                keypad.illuminate((8),0,255,0)
                keypad.update()
            if buttons == [9]:
                keypad.illuminate((9), 0,255,0)
                keypad.update()
            if buttons == [10]:
                keypad.illuminate((10), 0,255,0)
                keypad.update()
            if buttons == [11]:
                keypad.illuminate((11), 0,255,0)
                keypad.update()
        if colors == 'blue':    
            if buttons == [0]:
                keypad.illuminate((0), 0,0,255)
                keypad.update()
            if buttons == [1]:
                keypad.illuminate((1),0,0,255)
                keypad.update()
            if buttons == [2]:
                keypad.illuminate((2),0,0,255)
                keypad.update()
            if buttons == [3]:
                keypad.illuminate((3), 0,0,255)
                keypad.update()
            if buttons == [4]:
                keypad.illuminate((4),  0,0,255)
                keypad.update()
            if buttons == [5]:
                keypad.illuminate((5), 0,0,255)
                keypad.update()
            if buttons == [6]:
                keypad.illuminate((6), 0,0,255)
                keypad.update()
            if buttons == [7]:
                keypad.illuminate((7), 0,0,255)
                keypad.update()
            if buttons == [8]:
                keypad.illuminate((8), 0,0,255)
                keypad.update()
            if buttons == [9]:
                keypad.illuminate((9), 0,0,255)
                keypad.update()
            if buttons == [10]:
                keypad.illuminate((10), 0,0,255)
                keypad.update()
            if buttons == [11]:
                keypad.illuminate((11), 0,0,255)
                keypad.update()
        
        last_states = states
    
    time.sleep(0.1)







