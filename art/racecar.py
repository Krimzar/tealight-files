from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, tan, pi, sqrt, acos, atan, asin, radians, degrees

print screen_width / 2
print screen_height / 2

car1 = None

class car:

  CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
  TotalOrientation = 0.0 #Initialisation of total orientation moved by the car
  Acceleration = 0.0 #Initialisation of acceleration as a float
  Speed = 0.0 #Initialisation of speed as a float
  Friction = 0.003 #Initialisation of friction constant
  
  AngleA = 0.0 #Initialises angles and distances needed for trigonometric calculcations
  AngleB = 0.0
  AngleC = 0.0
  DistAD = 0.0
  DistBD = 0.0
  DistCD = 0.0
  
  
  CoordCentre["x"] = screen_width / 2 #Determines centre of the screen as (x,y)
      
  CoordCentre["y"] = screen_height / 2
  

  CoordA = {"x": (CoordCentre["x"]-14), "y": (CoordCentre["y"]+16)}   
  CoordB = {"x": (CoordCentre["x"]-16), "y": (CoordCentre["y"]-13)} 
  CoordC = {"x": (CoordCentre["x"]+3), "y": (CoordCentre["y"])}                                              
  CoordD = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"])} 
  #Initialise car coordinates
  
  
  DistAD = sqrt((((CoordA["x"] - CoordD["x"])**2) + ((CoordA["y"] - CoordD["y"])**2)))
  DistBD = sqrt((((CoordB["x"] - CoordD["x"])**2) + ((CoordB["y"] - CoordD["y"])**2)))
  DistCD = CoordD["x"] - CoordC["x"] #Trigonometry to calculate orientation of racecar
  
  AngleA = atan((CoordD["x"] - CoordA["x"]) / (CoordD["y"] - CoordA["y"]))
  AngleB = atan((CoordD["x"] - CoordB["x"]) / (CoordD["y"] - CoordB["y"]))
  
  def draw_car(self):
    
    color("red")
      
    line(self.CoordA["x"], self.CoordA["y"], self.CoordB["x"], self.CoordB["y"])
    line(self.CoordA["x"], self.CoordA["y"], self.CoordD["x"], self.CoordD["y"])
    line(self.CoordB["x"], self.CoordB["y"], self.CoordD["x"], self.CoordD["y"])
    line(self.CoordA["x"], self.CoordA["y"], self.CoordC["x"], self.CoordC["y"])
    line(self.CoordB["x"], self.CoordB["y"], self.CoordC["x"], self.CoordC["y"])
    line(self.CoordD["x"], self.CoordD["y"], self.CoordC["x"], self.CoordC["y"])
    #Initialise lines of car
  
    
  def change_orientation(self, Orientation): 
    
    self.TotalOrientation += Orientation
    
    self.AngleA += radians(Orientation)
    self.AngleB += radians(Orientation)
    self.AngleC += radians(Orientation) 
    
    self.CoordA["x"] = ((self.DistAD * sin(self.AngleA)) + self.CoordD["x"])
    self.CoordA["y"] = ((self.DistAD * cos(self.AngleA)) + self.CoordD["y"])
    
    self.CoordB["x"] = ((self.DistBD * sin(self.AngleB)) + self.CoordD["x"])
    self.CoordB["y"] = ((self.DistBD * cos(self.AngleB)) + self.CoordD["y"])
    
    self.CoordC["x"] = ((self.DistCD * sin(self.AngleC)) + self.CoordD["x"])
    self.CoordC["y"] = ((self.DistCD * cos(self.AngleC)) + self.CoordD["y"])
    
    print("Ax:" , self.CoordA["x"])
    print("Ay:" , self.CoordA["y"])
    print("Bx:" , self.CoordB["x"])
    print("By:" , self.CoordB["y"])
    print("Cx:" , self.CoordC["x"])
    print("Cy:" , self.CoordC["y"])
    print("Dx:" , self.CoordD["x"])
    print("Dy:" , self.CoordD["y"])
  
  def update_speed(self):
    if self.Speed > 1.0:
      self.Speed = 1.0
    else:
      self.Speed += self.Acceleration
    if self.Acceleration  > 0:
      self.Acceleration -= (self.Friction * self.Speed)
    
    
    self.ChangeY = -cos(radians(self.TotalOrientation)) * self.Speed
    self.ChangeX = -sin(radians(self.TotalOrientation)) * self.Speed
    
    self.CoordA["x"] += self.ChangeX
    self.CoordA["y"] += self.ChangeY
    
    self.CoordB["x"] += self.ChangeX
    self.CoordB["y"] += self.ChangeY
    
    self.CoordC["x"] += self.ChangeX
    self.CoordC["y"] += self.ChangeY
    
    self.CoordD["x"] += self.ChangeX
    self.CoordD["y"] += self.ChangeY
    
    
  
    
def start():
  global car1
  car1 = car()
  
def handle_keydown(key):
  global car1
  
  if key == "left":   
    car1.change_orientation(5)
  elif key == "right":
    car1.change_orientation(-5)
  elif key == "up": 
    if car1.Acceleration > 0.05: 
      car1.Acceleration = 0.05
    else:
      car1.Acceleration += 0.01
      
def handle_frame():
  global car1
  
  car1.update_speed()
  color("white")
  box(0, 0, 10000, 10000)
  car1.draw_car()
  

start()



