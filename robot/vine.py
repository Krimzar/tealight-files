from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



thing = touch() #Initialise
count = smell() 
path = 0

global path


#def TurnRobot(IsFruit, path):
  
  #if left_side() == "fruit":
  #  turn(3)

 # elif right_side() == "fruit":
   # turn(1)
  
 # if IsFruit == False: 
   # turn(-2)
    

def MoveRobot(): 
  
  if left_side() == "fruit":
    turn(3)
  elif right_side() == "fruit":
    turn(1)
  move()
  
  path += 1
  
  if smell() > 0: 
    MoveRobot()
  else: 
    for i in range(path):
      turn(-2)
      move()
      path -= 1
  MoveRobot()
  
MoveRobot()
    
  
  