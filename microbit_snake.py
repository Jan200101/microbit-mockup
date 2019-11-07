# Add your Python code here. E.g.
from microbit import *
import random

class Retard(Exception):
    pass
        
# size of the thing
size = (5, 5)

class Pallet:
    def __init__(self):
        self.x = random.randint(0, size[0]-1)
        self.y = random.randint(0, size[1]-1)


pallet = None
# positions
x = 2
y = 2

# 0 north
# 1 east
# 2 south
# 3 west 
direction = 1

a_pressed = False
b_pressed = False

timer = 0

while True:
    if button_a.is_pressed():
        if not a_pressed:
            a_pressed = True
            direction = (direction - 1) % 4
    else:
        if a_pressed:
            a_pressed = False
    
    if button_b.is_pressed():
        if not b_pressed:
            b_pressed = True
            direction = (direction + 1) % 4
    else:
        if b_pressed:
            b_pressed = False
            
    if a_pressed and b_pressed:
        reset()
        
    if not pallet:
        pallet = Pallet()
        
    buffer = ""
    for height in range(0, size[1]):
        for width in range(0, size[0]):
            if x == width and y == height:
                buffer += '9'
                if pallet.x == width and pallet.y == height:
                    pallet = None
            else:
                if pallet != None and pallet.x == width and pallet.y == height:
                    buffer += '4'
                else:
                    buffer += '0'
                
        buffer += ":"
        
    buffer = Image(buffer)
    
    if timer >= 10:
        timer = 0
        display.show(buffer)
        
        if direction == 0:
            y = (y - 1) % size[1]
        elif direction == 1:
            x = (x + 1) % size[0]
        elif direction == 2:
            y = (y + 1) % size[1]
        elif direction == 3:
            x = (x - 1) % size[0]
        else:
            raise Retard()
        
    sleep(5)
    timer += 1
    
    
