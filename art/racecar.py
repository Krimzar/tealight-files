from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, tan, pi, sqrt, acos, atan, asin, radians, degrees

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
TotalOrientation = 0.0
Acceleration = 0.0 #Initialisation of oritenation and acceleration as floats
Speed = 0.0 
Friction = 0.003

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
CoordC = {"x": (CoordCentre["x"]+30), "y": (CoordCentre["y"])}                                              
CoordD = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"])} 
#Initialise car coordinates
#AD BD CD

DistAD = sqrt((((CoordA["x"] - CoordD["x"])**2) + ((CoordA["y"] - CoordD["y"])**2)))
DistBD = sqrt((((CoordB["x"] - CoordD["x"])**2) + ((CoordB["y"] - CoordD["y"])**2)))
DistCD = CoordD["x"] - CoordC["x"]

AngleA = atan((CoordD["x"] - CoordA["x"]) / (CoordD["y"] - CoordA["y"]))
AngleB = atan((CoordD["x"] - CoordB["x"]) / (CoordD["y"] - CoordB["y"]))

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
  
  global AngleA, AngleB, AngleC, DistAD, DistBD, DistCD, TotalOrientation
  
  TotalOrientation += Orientation
  
  AngleA += radians(Orientation)
  AngleB += radians(Orientation)
  AngleC += radians(Orientation) 
  
  CoordA["x"] = ((DistAD * sin(AngleA)) + CoordD["x"])
  CoordA["y"] = ((DistAD * cos(AngleA)) + CoordD["y"])
  
  CoordB["x"] = ((DistBD * sin(AngleB)) + CoordD["x"])
  CoordB["y"] = ((DistBD * cos(AngleB)) + CoordD["y"])
  
  CoordC["x"] = ((DistCD * sin(AngleC)) + CoordD["x"])
  CoordC["y"] = ((DistCD * cos(AngleC)) + CoordD["y"])

def update_speed():
  global Speed, TotalOrientation, Acceleration
  if Speed > 1.0:
    Speed = 1.0
  else:
    Speed += Acceleration
  if Acceleration  > 0:
    Acceleration -= (Friction * Speed)
  
  
  ChangeY = -cos(radians(TotalOrientation)) * Speed
  ChangeX = -sin(radians(TotalOrientation)) * Speed
  
  CoordA["x"] += ChangeX
  CoordA["y"] += ChangeY
  
  CoordB["x"] += ChangeX
  CoordB["y"] += ChangeY
  
  CoordC["x"] += ChangeX
  CoordC["y"] += ChangeY
  
  CoordD["x"] += ChangeX
  CoordD["y"] += ChangeY
  
  
def handle_keydown(key): 
  global Angle, Acceleration
  if key == "left":   
    change_orientation(5)
  elif key == "right":
    change_orientation(-5)
  elif key == "up": 
    if Acceleration > 0.05: 
      Acceleration = 0.05
    else:
      Acceleration += 0.01
    
    
    
    

    
    
    
def handle_frame():
  update_speed()
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


