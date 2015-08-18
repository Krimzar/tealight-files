from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



thing = look() #Initialise
count = smell()

while count > 0: 
  if left_side() == "fruit":
    turn(3)
  elif right_side() == "fruit":
    turn(1)
  move()

  thing = look()
  count = smell()
  



#thing = look()
#print(thing)