Due to the fact that .png picture file have different bit depth when storaging.

The official resources are given in 8-bit when all color displayed is color in picture.

Yet when making my own pictures, the picture color is twisted.

Solving this, use the colswap function within inkyphat.show_image() function.

In this case, the colswap = [1,0,2] to correct the display color.

For more detial, visit http://docs.pimoroni.com/inkyphat/index.html#
