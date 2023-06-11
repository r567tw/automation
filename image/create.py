from PIL import Image  
import webcolors

width = 400
height = 300

def color_name_to_rgb(color_name):
    try:
        color = webcolors.name_to_rgb(color_name)
        return color
    except ValueError:
        return None

color_name = input("請輸入顏色名稱：")

rgb_color = color_name_to_rgb(color_name)


if rgb_color is not None:
    img  = Image.new( mode = "RGB", size = (width, height), color = (rgb_color[0], rgb_color[1], rgb_color[2]) )
    img.save("{}.gif".format(color_name))
else:
    print("Not Valid Color")