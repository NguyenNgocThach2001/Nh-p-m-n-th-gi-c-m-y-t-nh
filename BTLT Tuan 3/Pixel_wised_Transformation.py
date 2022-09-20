import cv2

def resize(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

def transpose_image(img):
    transpose_image = img.copy()
    width = img.shape[1]
    height = img.shape[0]
    for i in range(width):
        for j in range(height):
            transpose_image[j][i] = img[i][j]
    return transpose_image


img1 = cv2.imread("image/input.jpg")
img1 = resize(img1, 20)
img2 = cv2.imread('image/input1.jpg')
img3 = cv2.imread('image/input2.jpg')

img_vertical_flip = img1[::-1]
img_horizontal_flip = img1[::,::-1]
img_diagonal_flip = transpose_image(img1)
cv2.imshow("input",img1)
cv2.imshow("vertical_flip", img_vertical_flip)
cv2.imshow("horizontal_flip", img_horizontal_flip)
cv2.imshow("diagonal_flip", img_diagonal_flip)

h1,w1,c1 = img2.shape
h2,w2,c2 = img3.shape
h= int(min(h1,h2) * 20 / 100)
w= int(min(w1,w1) * 20 / 100)
img2 = cv2.resize(img2,(w,h))
img3 = cv2.resize(img3,(w,h))

while(True):
    Speed = 4
    for D in range(0,w+1,Speed):
        result=img2.copy()
        result[:,0:D,:]=img2[:,w-D:w,:]
        result[:,D:w,:]=img3[:,D:]
        cv2.imshow("Cover And Uncover From Left",result)
        cv2.waitKey(10)

    for D in range(0,w+1,Speed):
        result=img2.copy()
        result[:,0:w-D,:] = img2[:,D:w,:]
        result[:,w-D:w,:] = img3[:,w-D:w,:]
        cv2.imshow("Cover And Uncover From Left",result)
        cv2.waitKey(10)
