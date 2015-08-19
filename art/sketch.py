from tealight.art import (color, line, spot, circle, box, image, text, background)

lastx = 0
lasty = 0



def handle_mousedown(x,y):
  global lastx, lasty
  
  lastx = x
  lasty = y

def handle_mousemove(x,y,button):
  global lastx, lasty
  
  if button == "left":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    color("black")
    
  elif button == "right":
    line(lastx, lasty, x, y)
    lastx = x
    lasty = y
    hue = 0
    color(hue)
    hue + 1
  