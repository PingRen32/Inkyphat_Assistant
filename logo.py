from PIL import Image
import sys
import inkyphat

inkyphat.set_colour("yellow")
inkyphat.set_border(inkyphat.BLACK)
inkyphat.set_image(Image.open("resources/InkyPhat-212x104.png"))

inkyphat.show()
