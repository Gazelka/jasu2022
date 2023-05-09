from PIL import Image, ImageDraw
import math

#base colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

def y(k,x):
    return k*x

def sweep(img):
    size = img.size
    image = img.copy()
    draw = ImageDraw.Draw(image)
    for n in range(0,size[0],100):
            for i in range(2, 180):
                k = math.tan(math.degrees(i))
                flag = True
                x = 0
                while (x+n < size[0]) and (abs(int(k * x)) < size[1]):
                    curr = img.getpixel((x+n, abs(int(k * x))))
                    if (curr[0] == 0 and curr[1] == 0 and curr[2] == 0):
                        flag = False
                        break
                    x += 1
                if flag:
                    draw.line((n, 0, x+n, abs(int(k * x))), fill=red, width=1)
    return image


if __name__ == '__main__':
    img = Image.open('result2.png')
    sweep(img).save("sweepline3.png", "PNG")