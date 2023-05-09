from PIL import Image
from random import randint

def visual(arr,x):
    background = Image.open('example_2.jpg')
    for i in range(len(arr)):
        overlay = Image.open('all_types/type_'+str(arr[i])+'_'+str(i)+'.png')
        background.paste(overlay, (0, 0), overlay)
    background.save("results2/result"+str(x)+".png")


if __name__ == '__main__':
    l = [[1],[4],[8,9],[2],[6],[0,7]]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                x = l[i][0]
                y = l[j][0]
                z = l[k][0]
                if (len(l[i]) >1):
                    x=l[i][randint(0,1)]
                if len(l[j])>1:
                    y=l[j][randint(0,1)]
                if len(l[k])>1:
                    z=l[k][randint(0,1)]
                if not (x==y or y==z or x==z):
                    visual([x,y,y,z,z,x,x,z,z,y],str(i+1)+str(j+1)+str(k+1)+"_0")
                    visual([x, x, y, z, z, y, y, z, z, y], str(i + 1) + str(j + 1)+str(k+1)+"_1")
                    visual([x, x, y, y, y, y, z, z, z, z], str(i + 1) + str(j + 1) + str(k + 1) + "_2")



