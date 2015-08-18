from tealight.logo import move, turn

def polygon(edges, size):
  angle = (360.0 / edges)
  for i in range(0, edges):
    move(size)
    turn(angle)
 
def DrawChessboard(width):
  for i in range(0, width):
      
    polygon(4,40)
    move(40)
    #turn(90)

      

DrawChessboard(8)

#angle = 360 / edges
#  decoration = size / 2
#  for i in range(0, edges):
#    move(size)
#    square(decoration)
#    turn(angle)