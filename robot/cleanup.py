from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

while smell() > 0: 
  if left_side() == "fruit":
    turn(-1)
  elif right_side() == "fruit":
    turn(1)
  move()
  