import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_eu.avi', fourcc, 20.0, (640,360))

print(cap.isOpened())
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        print(str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" x "+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('FRAMES', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()