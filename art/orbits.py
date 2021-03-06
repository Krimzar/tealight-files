from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0
hue = 0

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = -power
  elif key == "down":
    ay = power

def handle_keyup(key):
  global ax, ay

  if key == "left" or key == "right":
    ax = 0
  elif key == "up" or key == "down":
    ay = 0.01
    
def handle_frame():
  global x,y,vx,vy,ax,ay, hue
  
  ax = ax - 0.01 * (x - (screen_width/2))
  ay = ay - 0.01 * (y - (screen_height/2))
  
  if ax > 0.01 or ax < 0.01:
    ax = 0.01
  
  if ay > 0.01 or ay < 0.01:
    ay = 0.01
  
  color("hsl(%d,100%%,50%%)" % hue)
  
  hue += 1
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  if x > screen_width:
    vx = vx * -1
    
  if y > screen_height:
    vy = vy * -1
    
  if x < 0:
    vx = vx * -1
    
  if y < 0:
    vy = vy * -1
  
  color("hsl(%d,100%%,50%%)" % hue)
  
  spot(x,y,8)
  
  
