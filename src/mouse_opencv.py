from matplotlib import pyplot as plt
import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)
font = cv2.FONT_HERSHEY_SIMPLEX

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = str(x)+', '+str(y)
        cv2.putText(img, strXY, (x,y), font, .5, (0,255,255), 2)
        cv2.imshow("IMAGEM", img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        strXY = str(b)+', '+str(g)+', '+str(r)
        cv2.putText(img, strXY, (x,y), font, .5, (255,0,255), 2)
        cv2.imshow("IMAGEM", img)
        


# img = np.zeros([512,512,3], np.uint8)
img = cv2.imread('./imgs/pessoa.jpg')
cv2.imshow("IMAGEM", img)


cv2.setMouseCallback("IMAGEM", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()