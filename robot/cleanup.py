from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def MoveRobot():

  while smell() > 0: 
    if left_side() == "fruit":
      turn(-1)
    elif right_side() == "fruit":
      turn(1)
    move()
  
  else:
    turn(2)
    move()
    MoveRobot()
    
MoveRobot()
  