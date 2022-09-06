from webbrowser import get
import cv2 as cv
import time

def draw_triangle(x, y, z, img):
    color = (255, 250, 255)
    thickness = 1
    img = cv.line(img, x, y, color, thickness)
    img = cv.line(img, x, z, color, thickness)
    img = cv.line(img, y, z, color, thickness)
    return img

def get_mid_point(x, y):
    return (int((x[0] + y[0]) / 2), int((x[1] + y[1]) / 2))

def draw_sierpinski_triangle(A, B, C, img, cnt):
    if (cnt == 0):
        return 
    
    MAB = get_mid_point(A,B)
    MAC = get_mid_point(A,C)
    MBC = get_mid_point(B,C)
    draw_triangle(MAB, MAC, MBC, img)

    draw_sierpinski_triangle(A,MAB,MAC,img, cnt - 1)
    draw_sierpinski_triangle(MAB,B,MBC,img, cnt - 1)
    draw_sierpinski_triangle(MAC,MBC,C,img, cnt - 1)

path = r"image/A_black_image.jpg"
img = cv.imread(path)
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
triangle_edge = min(height,width)

triangle_top_point = (int(abs(width) / 2), int(abs(triangle_edge) / 2  - triangle_edge / 4))
triangle_right_down_point = (int(abs(width - triangle_edge) / 2 + triangle_edge), int(abs(height - triangle_edge) / 2 + triangle_edge  - triangle_edge / 4))
triangle_left_down_point = (int(abs(width - triangle_edge) / 2), int(abs(height - triangle_edge) / 2 + triangle_edge   - triangle_edge / 4))

img = draw_triangle(triangle_left_down_point, triangle_top_point, triangle_right_down_point, img)
draw_sierpinski_triangle(triangle_left_down_point, triangle_top_point, triangle_right_down_point, img, 2)

# Displaying the image
cv.imshow('image', img)
cv.waitKey(0)
