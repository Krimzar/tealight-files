from tealight.logo import move, turn

def polygon(edges, size):
  angle = (360.0 / edges)
  for i in range(0, edges):
    move(size)
    turn(angle)
 
def DrawChessboard(length):
  for i in range(0, length):
      
    polygon(4,40)
    move(40)




DrawChessboard(8)
turn(180)
DrawChessboard(8)
turn(-90)
move(80)
turn(-90)


#angle = 360 / edges
#  decoration = size / 2
#  for i in range(0, edges):
#    move(size)
#    square(decoration)
#    turn(angle)