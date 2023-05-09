from PIL import Image

def read_points(img):
    arr = []
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pres_pix = img.getpixel((i,j))
            if (pres_pix[0] == 0 and pres_pix[1] == 0 and pres_pix[2] == 0):
                arr.append([j, i])
    return arr

if __name__ == '__main__':
    img = Image.open('triang.png')
    points = read_points(img)
    with open("points.txt") as file:
        sys.stdout = file
        for i in points:
            print(i[0],i[1])
        sys.stdout = original_stdout