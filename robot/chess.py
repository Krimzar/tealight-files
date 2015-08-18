from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



thing = look() #Initialise
while thing == "fruit":
  move()
  thing = look()
  




#thing = look()
#print(thing)