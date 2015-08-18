from tealight.logo import move, turn

def polygon(edges, size):
  angle = (360.0 / edges)
  for i in range(0, edges):
    move(size)
    turn(angle)
 
def DrawChessboard(width, length):
  for i in range(0, length):
    for i in range(0, width):
      polygon(4,60)
      move(60)
    turn(90)

      
     
DrawChessboard(8,8)   

#angle = 360 / edges
#  decoration = size / 2
#  for i in range(0, edges):
#    move(size)
#    square(decoration)
#    turn(angle)