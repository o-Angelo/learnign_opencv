from matplotlib import pyplot as plt
import numpy as np
import cv2

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def main():
    # obj_img = cv2.imread("./imgs/pessoa.jpg")
    obj_img = np.zeros([512,512,3], np.uint8)

    obj_img = cv2.line(obj_img, (0,0), (150,150), (255,0,0), 5)
    obj_img = cv2.arrowedLine(obj_img, (0,150), (150,150), (255,150,94), 5)
    obj_img = cv2.rectangle(obj_img, (200,100), (400,200), (150,87,120),5)
    obj_img = cv2.circle(obj_img, (300,300), 50, (84,155,65), -1)

    obj_img = cv2.putText(obj_img, "Ola mundo!", (0,350), cv2.FONT_HERSHEY_SIMPLEX, 3, (64,58,120), 5, cv2.LINE_AA)

    showImg(obj_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
