from tealight.logo import move, turn

def polygon(edges, size):
  angle = (360.0 / edges)
  for i in range(0, edges):
    move(size)
    turn(angle)
 
def DrawChessboard(width, length):
  for i in range(0,8):
    for i in range(0,8):
      polygon(4,150)
      move(1)
      polygon(4,150)
      turn(angle)
     
    

