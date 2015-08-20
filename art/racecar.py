from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre

CoordCentre["x"] = screen_width / 2
CoordCentre["y"] = screen_height / 2



color("red")

CoordA = {"x": CoordCentre["x"], "y": CoordCentre["y"]}   
CoordB = {"x": CoordCentre["x"], "y": (CoordCentre["y"]-5)} 
CoordC = {"x": (CoordCentre["x"]+10), "y": (CoordCentre["y"]-2.5)}                                              
CoordD = {"x": (CoordCentre["x"]+5), "y": (CoordCentre["y"]-2.5)} 

#del point["#"] to delete a point


print(CoordA["x"])

line(CoordA["x"], CoordA["y"], CoordB["x"], CoordA["y"])
spot(CoordCentre["x"],CoordCentre["y"],200)

