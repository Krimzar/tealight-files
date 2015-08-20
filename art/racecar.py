from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, pi

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
InitCount = False
Angle = 0.0
Acceleration = 0.0 #Initialisation of angle and acceleration as floats
ChangeInX = 0
ChangeInY = 0
Power = 0.3

#del point["#"] to delete a point

def draw_car(CoordCentre, InitCount):
  
  color("red")

  CoordCentre["x"] = screen_width / 2
    
  CoordCentre["y"] = screen_height / 2
    
  CoordA = {"x": (CoordCentre["x"]-15-ChangeInX), "y": (CoordCentre["y"]+15-ChangeInY)}   
  CoordB = {"x": (CoordCentre["x"]-15-ChangeInX), "y": (CoordCentre["y"]-15-ChangeInY)} 
  CoordC = {"x": (CoordCentre["x"]+30-ChangeInX), "y": (CoordCentre["y"]-ChangeInY)}                                              
  CoordD = {"x": (CoordCentre["x"]-ChangeInX), "y": (CoordCentre["y"]-ChangeInY)} 
  #Initialise car coordinates
    
    
  line(CoordA["x"], CoordA["y"], CoordB["x"], CoordB["y"])
  line(CoordA["x"], CoordA["y"], CoordD["x"], CoordD["y"])
  line(CoordB["x"], CoordB["y"], CoordD["x"], CoordD["y"])
  line(CoordA["x"], CoordA["y"], CoordC["x"], CoordC["y"])
  line(CoordB["x"], CoordB["y"], CoordC["x"], CoordC["y"])
  line(CoordD["x"], CoordD["y"], CoordC["x"], CoordC["y"])
  #Initialise lines of car

    
 

def handle_frame():
  
  global Power, CoordA, CoordB, CoordC, CoordD, Angle, Acceleration, CoordCentre, ChangeInX, ChangeInY
  Acceleration = Acceleration - (0.01 * (screen_width/2))
  
  if Acceleration > 0.01 or Acceleration < 0.01:
    Acceleration = 0.01
    
  draw_car(CoordCentre, InitCount)
  
  ChangeInX += Acceleration
  
  ChangeInY += Acceleration
  

def handle_keydown(key): 
  global Power
  if key == "up": #UP for acceleration key 
    Acceleration = power
  
  
def handle_keyup(key):
  global Acceleration
  if key == "up": 
    Acceleration = 0



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


