from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

from time import sleep

thing = look() #Initialise
count = smell()


def IfFood(Side):
  if Side == "left":
    turn(3)
  elif Side == "right":
    turn(1)
  move()

while count > 0: 
  if touch() == "fruit": 
    IfFood("front")
  elif left_side() == "fruit":
    IfFood("left")
  elif right_side == "fruit":
    IfFood("right")
  sleep(1)
  thing = look()
  count = smell()
  



#thing = look()
#print(thing)