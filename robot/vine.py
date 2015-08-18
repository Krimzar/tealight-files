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

def TurnRobot(IsFruit):
  if left_side() == "fruit":
    turn(3)

  elif right_side() == "fruit":
    turn(1)

  if IsFruit == "NoFruit":
    for i in range(0,2):
      turn(-1)
      move()
      
    

def MoveRobot(): 
  while smell() > 0: 
    TurnRobot()
    move()
  else: 
    TurnRobot("NoFruit")
    MoveRobot()
    
  
  FruitSide = CheckFruit()
  
MoveRobot()
  