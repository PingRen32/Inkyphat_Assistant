import sys
from PIL import ImageFont
from PIL import Image
import inkyphat

inkyphat.set_colour("yellow")
inkyphat.set_border(inkyphat.BLACK)

inkyphat.set_image("resources/ShibaInu_resources/display_ShibaInu.png",colswap=[2,0,1])

font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 20)
message = "Hi"

w, h = font.getsize(message)
x = 64
y = 24
inkyphat.text((x, y), message, inkyphat.RED, font)
inkyphat.show()
