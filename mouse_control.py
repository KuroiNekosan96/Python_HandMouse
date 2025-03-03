import cv2
import mediapipe
import pyautogui

captura_manos=mediapipe.solutions.hands.Hands() #capturo las manos
op_dibujo=mediapipe.solutions.drawing_utils #dibujo los movimientos


cam=cv2.VideoCapture(0) #utilizo la primera camara de mi pc
while True:
    _,image = cam.read() #capturo la camara
    image=cv2.flip(image,1) #posicion 1 eje vert
    rgb_image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convertir imagen a rgb
    salida_manos= captura_manos.process(rgb_image)#capturo las manos
    all_hands= salida_manos.multi_hand_landmarks #capturo todas las manos

    #valida si hay manos
    if all_hands:
        #que capture una por una
        for hand in all_hands:
            op_dibujo.draw_landmarks(image,hand)

    cv2.imshow("captura de video de los movimientos de la mano",image)
    key=cv2.waitKey(100)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()



