import cv2
import numpy as np


#base colors
white = (255,255,255)
black = (0,0,0)

def dist(x, y):
    return(pow(pow(x,2)+pow(y,2),0.5))

def read_points(img):
    arr = []
    for i in range(size[0]):
        for j in range(size[1]):
            pres_pix = img[i,j]
            if (pres_pix[0] == 0 and pres_pix[1] == 0 and pres_pix[2] == 0):
                print(pres_pix)
                arr.append((j,i))
    return arr



def rect_contains(rect, point) :
    if point[0] < rect[0] :
        return False
    elif point[1] < rect[1] :
        return False
    elif point[0] > rect[2] :
        return False
    elif point[1] > rect[3] :
        return False
    return True

def draw_point(img, p, color ) :
    cv2.circle( img, p, 1, color, 1, cv2.FILLED, 0 )


def draw_voronoi(img, subdiv):
    (facets, centers) = subdiv.getVoronoiFacetList([])
    for i in range(len(facets)):
        ifacet_arr = []
        for f in facets[i]:
                ifacet_arr.append(f)

        ifacet = np.array(ifacet_arr, int)
        color = white
        cv2.fillConvexPoly(img, ifacet, color, cv2.LINE_8, 0)
        ifacets = np.array([ifacet])
        cv2.polylines(img, ifacets, True, (0, 0, 0), 4, cv2.LINE_8, 0)
        cv2.circle(img, (int(centers[i][0]), int(centers[i][1])), 3, (0, 0, 0), 1,cv2.FILLED, 0)

'''
def draw_voronoi(img, subdiv, fill_color, voronoi_color) :

    ( facets, centers) = subdiv.getVoronoiFacetList([])
    for i in range(len(facets)) :
        temp_facet = []
        for f in facets[i] :
            temp_facet.append(f)

        copy_facet = np.array(temp_facet, int)
        cv2.fillConvexPoly(img, copy_facet, fill_color, cv2.LINE_8, 0)
        ifacets = np.array([copy_facet])
        cv2.polylines(img, ifacets, True, voronoi_color, 2, cv2.LINE_8, 0)
        draw_point(img,(int(centers[i][0]),int(centers[i][1])),voronoi_color)
'''

def draw_delaunay(img, subdiv, delaunay_color ) :

    triangleList = subdiv.getTriangleList()
    size = img.shape

    r = (0, 0, size[1], size[0])

    for t in triangleList :
        pt1 = (int(t[0]), int(t[1]))
        pt2 = (int(t[2]), int(t[3]))
        pt3 = (int(t[4]), int(t[5]))

        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3) :
            sections.append((pt1,pt2))
            sections.append((pt2, pt3))
            sections.append((pt1, pt3))



if __name__ == '__main__':

    win_delaunay = "Delaunay Triangulation"
    win_voronoi = "Voronoi Diagram"

    # Read in the image.
    img = cv2.imread("0802.png");

    img_orig = img.copy();
    size = img.shape
    print(size)
    rect = (0, 0, size[1], size[0])
    subdiv = cv2.Subdiv2D(rect);
    points = []
    adj_list = {}


    # Read in the points from a text file
    '''
    with open("points.txt") as file :
        for line in file :
            x, y = line.split()
            points.append((int(x), int(y)))
            '''
    points=read_points(img)


    # Insert points
    for p in points:
        subdiv.insert(p)
        adj_list.setdefault(p, set()).add(value)

    draw_delaunay(img, subdiv, black);

    # Draw points
    for p in points:
        draw_point(img, p, black)

    # allocation
    #img_voronoi = np.zeros(img.shape, dtype=img.dtype)

    #draw_voronoi(img_voronoi, subdiv)

    #show res
    cv2.imwrite('image_triangulation_part2.jpg', img)
    #cv2.imwrite('infrastucture_diag.png', img_voronoi)
    cv2.imshow(win_delaunay, img)
    #cv2.imshow(win_voronoi, img_voronoi)

    #end of program
    cv2.waitKey(0)