from matplotlib import pyplot as plt
import numpy as np
import cv2

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()


def main():
    obj_img = cv2.imread("./imgs/pessoa.jpg")

