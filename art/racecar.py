from tealight.art import (color, line, spot, circle, box, image, text, background)

#from tealight.art import screen_width, screen_height

#print screen_width
#print screen_height



color("#00CC00")

CoordA = {"x": 328, "y": 322}   #Initialise dictionary of car coordinates
CoordB = {"x": 328, "y": 317}
CoordC = {"x": 338, "y": 319.5}
CoordD = {"x": 333, "y": 319.5}

#del point["#"] to delete a point

line(CoordA["x"], CoordA["y"], CoordB["x"], CoordA["y"])
