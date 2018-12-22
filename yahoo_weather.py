from weather import Weather, Unit
import inkyphat
from PIL import Image, ImageDraw, ImageFont

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('west lafayette')

condition = location.condition
day, date, month, year, time, am_pm, zone = condition.date.split(" ")

inkyphat.set_colour("yellow")
inkyphat.set_border(inkyphat.BLACK)

img = Image.open("resources/ShibaInu_resources/cute.png")
draw = ImageDraw.Draw(img)
icon_image = Image.open("resources/Weather/"+str(condition.code)+".png")

font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 14)

draw.text((24, 12), day + " " + date + " " + month + " " + year, inkyphat.BLACK, font=font)
draw.text((24, 32), time + " " + am_pm + " " + zone, inkyphat.BLACK, font=font)
draw.text((64, 52), condition.text, inkyphat.BLACK, font=font)
draw.text((64, 72), condition.temp + " " + chr(176) + "C", inkyphat.BLACK, font=font)

img.paste(icon_image, (24, 56))

# Display the weather data on Inky pHAT
inkyphat.set_image(img,colswap=[2,0,1])
inkyphat.show()



