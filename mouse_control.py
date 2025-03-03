import cv2
import mediapipe
import pyautogui

cam=cv2.VideoCapture(0) #utilizo la primera camara de mi pc
while True:
    _,image = cam.read() #capturo la camara
    cv2.imshow("captura de video de los movimientos de la mano",image)
    key=cv2.waitKey(100)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()



