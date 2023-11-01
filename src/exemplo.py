from matplotlib import pyplot as plt
import numpy as np
import cv2

def showImg(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def getColor(img, x, y):
    return img.item(y,x,0), img.item(y,x,1), img.item(y,x,2)

def setColor(img, x, y, b, g, r):
    img.itemset((y, x, 0), b)
    img.itemset((y, x, 1), g)
    img.itemset((y, x, 2), r)
    return img

def main():
    obj_img = cv2.imread("./imgs/pessoa.jpg")
    altura, largura, cor = obj_img.shape
    print("Dimensões da Imagem: "+str(altura)+", "+str(largura))
    print("Canais de Cores: "+str(cor))

    for y in range(0, altura):
        for x in range(0, largura):
            azul, verde, vermelho = getColor(obj_img, x, y)
            obj_img = setColor(obj_img, x, y, 0, 0, vermelho)
    
    showImg(obj_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()