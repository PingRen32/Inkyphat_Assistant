import datetime
import time
import calendar
import sys
from PIL import Image, ImageFont
import inkyphat

inkyphat.set_colour("yellow")
inkyphat.set_border(inkyphat.BLACK)

text = Image.open("resources/calendar.png")
text_mask = inkyphat.create_mask(text, [inkyphat.WHITE])

inkyphat.set_image("resources/ShibaInu_resources/calendar_ShibaInu.png",colswap=[1,0,2])

cal = calendar.Calendar()
now = datetime.datetime.now()
dates = cal.monthdatescalendar(now.year, now.month)

col_w = 20
col_h = 13
cols = 7
rows = len(dates) + 1
cal_w = 1 + ((col_w + 1) * cols)
cal_h = 1 + ((col_h + 1) * rows)
cal_x = inkyphat.WIDTH - cal_w - 2
cal_y = 2

def print_digit(position, digit, colour):
    o_x, o_y = position

    num_margin = 2
    num_width = 6
    num_height = 7

    s_y = 11
    s_x = num_margin + (digit * (num_width + num_margin))

    sprite = text_mask.crop((s_x, s_y, s_x + num_width, s_y + num_height))
    inkyphat.paste(colour, (o_x, o_y), sprite)

def print_number(position, number, colour):
    """Prints a number using the sprite sheet."""

    for digit in str(number):
        print_digit(position, int(digit), colour)
        position = (position[0] + 8, position[1])

inkyphat.rectangle((cal_x, cal_y, cal_x + cal_w - 1, cal_y + cal_h - 1), fill=inkyphat.BLACK, outline=inkyphat.WHITE)

months_x = 2
months_y = 20
months_cols = 3
month_w = 23
month_h = 9

month_col = (now.month - 1) % months_cols
month_row = (now.month - 1) // months_cols
month_x = months_x + (month_col * month_w)
month_y = months_y + (month_row * month_h)
crop_region = (month_x, month_y, month_x + month_w, month_y + month_h)

month = text.crop(crop_region)
month_mask = text_mask.crop(crop_region)
monthyear_x = 28

for x in range(cols):
    o_x = (col_w + 1) * x
    o_x += cal_x

    crop_x = 2 + (16 * x)

    crop_region = ((crop_x, 0, crop_x + 16, 9))
    day_mask = text_mask.crop(crop_region)
    inkyphat.paste(inkyphat.WHITE, (o_x + 4, cal_y + 2), day_mask)

    o_x += col_w + 1
    inkyphat.line((o_x, cal_y, o_x, cal_h))

for y in range(rows):
    o_y = (col_h + 1) * y
    o_y += cal_y + col_h + 1
    inkyphat.line((cal_x, o_y, cal_w + cal_x - 1, o_y))

for row, week in enumerate(dates):
    y = (col_h + 1) * (row + 1)
    y += cal_y + 1

    for col, day in enumerate(week):
        x = (col_w + 1) * col
        x += cal_x + 1

        if (day.day, day.month) == (now.day, now.month):
            inkyphat.rectangle((x, y, x + col_w - 1, y + col_h - 1), fill=inkyphat.WHITE)
            print_number((x+3, y+3), day.day, inkyphat.BLACK)
        else:
            print_number((x+3, y+3), day.day, inkyphat.WHITE if day.month == now.month else inkyphat.RED)

inkyphat.show()
