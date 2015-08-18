from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

thing = touch()
count = smell() #Initialise

while count > 0:
  if touch() == "fruit":
    move()
  elif left_side() == "fruit":
    turn(3)
  elif right_side() == "fruit":
    turn(1)
  if touch() == "fruit":
    pass
  else:
    move()
  count = smell()