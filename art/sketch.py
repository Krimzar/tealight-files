from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

print screen_width
print screen_height
 
lastx = 0
lasty = 0
 
 
 
 
def handle_mousedown(x,y):
  global lastx, lasty
 
  lastx = x
  lasty = y
 
def handle_mousemove(x,y,button):
  global lastx, lasty
  print (lastx)
  print (lasty)
  if button == "left":
    color("black")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
  elif button == "right":
    color("red")
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y