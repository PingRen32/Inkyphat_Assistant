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

date_font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 14)
font = ImageFont.truetype(inkyphat.fonts.FredokaOne, 12)

draw.text((18, 12), day + " " + date + " " + month + " " + year, inkyphat.BLACK, font=date_font)
draw.text((18, 32), time + " " + am_pm + " " + zone, inkyphat.BLACK, font=date_font)
draw.text((50, 52), condition.text, inkyphat.BLACK, font=font)
draw.text((50, 72), condition.temp + " " + chr(176) + "C", inkyphat.BLACK, font=font)

img.paste(icon_image, (18, 52))

# Display the weather data on Inky pHAT
inkyphat.set_image(img,colswap=[2,0,1])
inkyphat.show()