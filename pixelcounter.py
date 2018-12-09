from PIL import Image
im = Image.open('imageJ.jpg')

black = 0
white = 0

for pixel in im.getdata():
    if pixel == (0, 0, 0): # if your image is RGB (if RGBA, (0, 0, 0, 255) or so
        black += 1
        white += 1
    else:
        white += 1
ratio = black/white
print('black=' + str(black)+', total='+str(white)+', ratio='+str(ratio))

# Karina - 4446.79
# Jordan - 6589.5
# Me - 6543.35