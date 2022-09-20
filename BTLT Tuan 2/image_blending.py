import cv2 
import sys

def image_size(img):
    height = img.shape[0]
    width = img.shape[1]
    return height, width

def main(scale = 0.2):
    origin_img = cv2.imread("image/origin.jpg")
    mask_img = cv2.imread("image/mask.png")
    effect_img = cv2.imread("image/effect1.jpg")

    height, width = image_size(origin_img)
    height = int(scale*height)
    width = int(scale*width)

    effect_img = effect_img[0:height, 0:width]
    origin_img = cv2.resize(origin_img, (width,height))
    mask_img = cv2.resize(mask_img, (width,height))
    result_img = origin_img.copy()


    print(image_size(origin_img))
    print(image_size(mask_img))
    print(image_size(effect_img))
    print(image_size(result_img))

    while(True):
        for k in range(20):
            alpha = 0.05 * k
            for i in range(height):
                for j in range(width):
                    if(mask_img[i][j][0] != 0):
                        result_img[i][j] = origin_img[i][j] * alpha + (1 - alpha) * effect_img[i][j]

            cv2.imshow("origin", origin_img)
            cv2.imshow("mask", mask_img)
            cv2.imshow("effect", effect_img)
            cv2.imshow("result", result_img)
            cv2.waitKey(20)

if __name__ == "__main__":
    scale = float(sys.argv[1])
    main(scale)
