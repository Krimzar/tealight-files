from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre

CoordCentre["x"] = screen_width / 2
CoordCenter["y"] = screen_height / 2



color("black")

CoordA = {"x": CoordCenter["x"], "y": CoordCenter["y"]}   
CoordB = {"x": CoordCenter["x"], "y": (CoordCenter["y"]-50)} 
CoordC = {"x": (CoordCenter["x"]+100), "y": (CoordCenter["y"]-25} 
CoordD = {"x": (CoordCenter["x"]+50), "y": (CoordCenter["y"]-25)} 

#del point["#"] to delete a point

line(CoordA["x"], CoordA["y"], CoordB["x"], CoordA["y"])

