from PIL import Image  

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height), color = (255, 255, 0) )
img.save("yellow.gif")