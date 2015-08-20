from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

color(00CC00)


CoordA = {"x": 0, "y": 10}   #Initialise dictionary of car coordinates
CoordB = {"x": 0, "y": 5}
CoordC = {"x": 10, "y": 7.5}
CoordD = {"x": 5, "y": 7.5}

#del point["#"] to delete a point

line(CoordA["x"], CoordA["y"], CoordB["x"], CoordA["y"])