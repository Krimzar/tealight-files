from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
Angle = 0.0
Acceleration = 0.0 #Initialisation of angle and acceleration as floats

CoordCentre["x"] = screen_width / 2
    
CoordCentre["y"] = screen_height / 2

#del point["#"] to delete a point

CoordA = {"x": (CoordCentre["x"]-15), "y": (CoordCentre["y"]+15)}   
CoordB = {"x": (CoordCentre["x"]-15), "y": (CoordCentre["y"]-15)} 
CoordC = {"x": (CoordCentre["x"]+30), "y": (CoordCentre["y"])}                                              
CoordD = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"])} 
#Initialise car coordinates

def draw_car():
  global CoordA, CoordB, CoordC, CoordD, CoordCentre
  
  color("red")
    
    
  line(CoordA["x"], CoordA["y"], CoordB["x"], CoordB["y"])
  line(CoordA["x"], CoordA["y"], CoordD["x"], CoordD["y"])
  line(CoordB["x"], CoordB["y"], CoordD["x"], CoordD["y"])
  line(CoordA["x"], CoordA["y"], CoordC["x"], CoordC["y"])
  line(CoordB["x"], CoordB["y"], CoordC["x"], CoordC["y"])
  line(CoordD["x"], CoordD["y"], CoordC["x"], CoordC["y"])
  #Initialise lines of car

def handle_keydown(key): 
  global CoordA, CoordB, CoordC, CoordD
  if key == "down": 
    CoordC["y"] += 50
    
def handle_frame():
  draw_car()
    
    
 




#def star(x, y, c, size, spines):
  
#  color(c)
  
 # angle = 0
  
#  for i in range(0, spines):
  #  x0 = x + (60 * cos(angle))
 #   y0 = y + (size * sin(angle))
    
 #   line(x, y, x0, y0)
    
 #   angle = angle + (2 * pi / spines)

#star(300, 300, "blue", 100, 50)
#star(600, 400, "purple", 200, 100)
#star(450, 200, "orange", 125, 30)


