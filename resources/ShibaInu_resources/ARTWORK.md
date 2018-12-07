# Content Information

All pictures inside this folder is personally made pixil arts inspired by several [Line stickers](https://store.line.me/stickershop/showcase/top/).


In the [artwork](https://github.com/PingRen32/Inkyphat_Assistant/tree/master/resources/ShibaInu_resources/artwork) folder contains all resourses I worked and will be working with.

All file .pixil could be import and work through [PixilArt](https://www.pixilart.com/) for modification.

Due to tri-color eink display color limitation, many complex stickers are currently classed as 'Unusable' (in 'Used' folder), but future adaption could be considered.

# Backgrounds PNG Information

All PNG files went through process of bit depth reduction through Adobe Photoshop CC.

You could check out original work in [my gallery](https://www.pixilart.com/pingrenworkhard/gallery).

## Code Twist

Due to the fact that .png picture file have different bit depth when storaging.

The official resources from Pimoroni are given in 8-bit when all color displayed is legit.

Yet when making my own pictures, the picture color is twisted even saved as 8-bit.

(Still haven't figure out a direct solution)

Solving this, use colswap within inkyphat.show_image() function.

In this case, I added a colswap = [1,0,2] to correct the display color.

All PNG files in this folder share this same twist.

For more detial, visit [Inkyphat API](http://docs.pimoroni.com/inkyphat/index.html#)

### Man, those Shiba Inu dogs are cute
