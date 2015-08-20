from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

print screen_width
print screen_height

CoordCentre = {"x": 0, "y": 0} #Initialise coordinates of car centre

CoordCentre["x"] = screen_width / 2
CoordCentre["y"] = screen_height / 2



color("red")

CoordA = {"x": CoordCentre["x"]-15, "y": (CoordCentre["y"]+15)}   
CoordB = {"x": CoordCentre["x"]-15, "y": (CoordCentre["y"]-15)} 
CoordC = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"]}                                              
CoordD = {"x": (CoordCentre["x"]), "y": (CoordCentre["y"])} 

#del point["#"] to delete a point


line(CoordA["x"], CoordA["y"], CoordB["x"], CoordB["y"])
#spot(CoordCentre["x"],CoordCentre["y"],200)

