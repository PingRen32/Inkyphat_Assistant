import inkyphat
import time
import sys

inkyphat.set_colour("yellow")
cycles = 2

colours = (inkyphat.RED, inkyphat.BLACK, inkyphat.WHITE)
colour_names= ("yellow", "black", "white")

for i in range(cycles):
    for j, c in enumerate(colours):
        inkyphat.set_border(c)
        for x in range(inkyphat.WIDTH):
            for y in range(inkyphat.HEIGHT):
                inkyphat.putpixel((x, y), c)
        inkyphat.show()
