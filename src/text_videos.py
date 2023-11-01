import cv2
import datetime

cap = cv2.VideoCapture(0)
print(str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" x "+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Largura: '+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+' Altura: '+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read() 
    if ret == True:
        data = str(datetime.datetime.now())
        cv2.putText(frame, data, (0,350), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow('FRAMES', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()