import cv2
import numpy

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
mov = cv2.VideoWriter('output.avi',fourcc,24.0,(1280,720))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720))
print(cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280))
#print(cap.get())
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret ==True:
        mov.write(frame)
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        cv2.imshow("Web Cam ",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
           


    else:
        break 

cap.release()

cv2.destroyAllWindows()
