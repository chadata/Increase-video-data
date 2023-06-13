import os
import cv2 as cv

dir_list = os.listdir(r"C:\Hands\\")

for i in dir_list:
    img = cv.imread(r"C:\Hands\\" + str(i))

    cv.imwrite(r"C:\Result\\" + str(i), img)

    img_flip_0 = cv.flip(img, 0)
    cv.imwrite(r"C:\Result\\" + "(1)" + str(i), img_flip_0)

    img_flip_1 = cv.flip(img, 1)
    cv.imwrite(r"C:\Result\\" + "(2)" + str(i), img_flip_1)

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img_gray_flip_0 = cv.flip(img_gray, 0)
    cv.imwrite(r"C:\Result\\" + "(3)" + str(i), img_gray_flip_0)

    img_gray_flip_1 = cv.flip(img_gray, 1)
    cv.imwrite(r"C:\Result\\" + "(4)" + str(i), img_gray_flip_1)
