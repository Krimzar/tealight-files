from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, tan, pi, sqrt, acos, atan, asin, radians, degrees

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
Orientation = 5.0
Acceleration = 0.0 #Initialisation of oritenation and acceleration as floats

AngleA = 0.0
AngleB = 0.0
AngleC = 0.0
DistAD = 0.0
DistBD = 0.0
DistCD = 0.0


CoordCentre["x"] = screen_width / 2
    
CoordCentre["y"] = screen_height / 2

#del point["#"] to delete a point

CoordA = {"x": (CoordCentre["x"]-15), "y": (CoordCentre["y"]+15)}   
CoordB = {"x": (CoordCentre["x"]-15), "y": (CoordCentre["y"]-15)} 
CoordC = {"x": (CoordCentre["x"]+30), "y": (CoordCentre["y"]+ 0.01)}                                              
CoordD = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"])} 
#Initialise car coordinates
#AD BD CD

DistAD = sqrt((((CoordA["x"] - CoordD["x"])**2) + ((CoordA["y"] - CoordD["y"])**2)))
DistBD = sqrt((((CoordB["x"] - CoordD["x"])**2) + ((CoordB["y"] - CoordD["y"])**2)))
DistCD = sqrt((((CoordC["x"] - CoordD["x"])**2) + ((CoordC["y"] - CoordD["y"])**2)))

AngleA = degrees(atan((CoordD["x"] - CoordA["x"]) / (CoordD["y"] - CoordA["y"])))
AngleB = degrees(atan((CoordD["x"] - CoordB["x"]) / (CoordD["y"] - CoordB["y"])))
AngleC = degrees(atan((CoordD["x"] - CoordC["x"]) / (CoordD["y"] - CoordC["y"])))

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

  
def change_orientation(Orientation): 
  
  global AngleA, AngleB, AngleC, DistAD, DistBD, DistCD
  
  AngleA += Orientation
  AngleB += Orientation
  AngleC += Orientation 
  
  CoordA["x"] += (DistAD * degrees(sin(AngleA)))
  CoordA["y"] += (DistAD * degrees(cos(AngleA)))
  
  CoordB["x"] += (DistBD * degrees(sin(AngleB)))
  CoordB["y"] += (DistBD * degrees(cos(AngleB)))
  
  CoordC["x"] += (DistCD * degrees(sin(AngleC)))
  CoordC["y"] += (DistCD * degrees(cos(AngleC)))

  
  
def handle_keydown(key): 
  global Angle
  if key == "left":   
    change_orientation(0.5)
    
    
def handle_frame():
  color("white")
  box(0, 0, 10000, 10000)
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


