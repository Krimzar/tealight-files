from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

from math import sin, cos, tan, pi, sqrt, acos, atan, asin, radians, degrees

from random import randint


class car:
  
  def __init__(self):
    
    self.Name = "" # Initialise name of car
    
    
    self.CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre
    self.TotalOrientation = 0.0 #Initialisation of total orientation moved by the car
    self.Acceleration = 0.0 #Initialisation of acceleration as a float
    self.Speed = 0.0 #Initialisation of speed as a float
    self.Friction = 0.003 #Initialisation of friction constant
    
    self.AngleA = 0.0 #Initialises angles and distances needed for trigonometric calculcations
    self.AngleB = 0.0
    self.AngleC = 0.0
    self.DistAD = 0.0
    self.DistBD = 0.0
    self.DistCD = 0.0
    
    self.CoordCentre["x"] = screen_width / 2 #Determines x coord of the centre of the screen
        
    self.CoordCentre["y"] = screen_height / 2 #Determines y coord of the centre of the screen
    
  
    self.CoordA = {"x": (self.CoordCentre["x"]-15), "y": (self.CoordCentre["y"]+15)}   
    self.CoordB = {"x": (self.CoordCentre["x"]-15), "y": (self.CoordCentre["y"]-15)} 
    self.CoordC = {"x": (self.CoordCentre["x"]+30), "y": (self.CoordCentre["y"])}                                              
    self.CoordD = {"x": (self.CoordCentre["x"]), "y": (self.CoordCentre["y"])} 
    #Initialise car coordinates
    
    
    self.DistAD = sqrt((((self.CoordA["x"] - self.CoordD["x"])**2) + ((self.CoordA["y"] - self.CoordD["y"])**2)))
    self.DistBD = sqrt((((self.CoordB["x"] - self.CoordD["x"])**2) + ((self.CoordB["y"] - self.CoordD["y"])**2)))
    self.DistCD = self.CoordD["x"] - self.CoordC["x"] 
    #Coordinate geometry to calculate the distances between points for each orientation
    
    
    self.AngleA = atan((self.CoordD["x"] - self.CoordA["x"]) / (self.CoordD["y"] - self.CoordA["y"]))
    self.AngleB = atan((self.CoordD["x"] - self.CoordB["x"]) / (self.CoordD["y"] - self.CoordB["y"]))
    #Above trigonometry to calculate the angles at points for each orientation 
  
  def draw_car(self, Name):
    
    RandomNumber = randint(1, 3)
    #Generate a random number between 1 and 3
    
    
    if RandomNumber == 1:
      color("red") #Random number 1 = set red
      
    elif RandomNumber == 2:
      color("green") #Random number 2 = set green
    
    elif RandomNumber == 3:
      color("blue") #Random number 3 = set blue
    
    text(self.CoordD["x"]-15, self.CoordD["y"]-35, self.Name)
    #Sets the name of the car to a string parameter passed to the method
 
    line(self.CoordA["x"], self.CoordA["y"], self.CoordB["x"], self.CoordB["y"])
    line(self.CoordA["x"], self.CoordA["y"], self.CoordD["x"], self.CoordD["y"])
    line(self.CoordB["x"], self.CoordB["y"], self.CoordD["x"], self.CoordD["y"])
    line(self.CoordA["x"], self.CoordA["y"], self.CoordC["x"], self.CoordC["y"])
    line(self.CoordB["x"], self.CoordB["y"], self.CoordC["x"], self.CoordC["y"])
    line(self.CoordD["x"], self.CoordD["y"], self.CoordC["x"], self.CoordC["y"])
    #Initialise lines of car
  
  def set_name(self, Name):
    
    self.Name = Name
    #Method to set the name of the car
    
  def change_orientation(self, Orientation): 
    
    self.TotalOrientation += Orientation
    #Calculates total orientation by addition of next orientation float
    
    self.AngleA += radians(Orientation)
    self.AngleB += radians(Orientation)
    self.AngleC += radians(Orientation) 
    
    self.CoordA["x"] = ((self.DistAD * sin(self.AngleA)) + self.CoordD["x"])
    self.CoordA["y"] = ((self.DistAD * cos(self.AngleA)) + self.CoordD["y"])
    
    self.CoordB["x"] = ((self.DistBD * sin(self.AngleB)) + self.CoordD["x"])
    self.CoordB["y"] = ((self.DistBD * cos(self.AngleB)) + self.CoordD["y"])
    
    self.CoordC["x"] = ((self.DistCD * sin(self.AngleC)) + self.CoordD["x"])
    self.CoordC["y"] = ((self.DistCD * cos(self.AngleC)) + self.CoordD["y"])
  
  def update_speed(self):
    if self.Speed > 2.0:
      self.Speed = 2.0
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
  elif key == "down":
    if car1.Acceleration == 0:
      if car1.Acceleration < -0.05:
        car1.Acceleration = -0.05
      else: 
        car1.Acceleration -= 0.01
      
def handle_frame():
  global car1
  
  car1.update_speed()
  color("white")
  box(0, 0, 10000, 10000)
  car1.draw_car()
  

start()



