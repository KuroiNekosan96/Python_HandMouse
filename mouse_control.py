import cv2
import mediapipe
import pyautogui

captura_manos=mediapipe.solutions.hands.Hands() #capturo las manos
op_dibujo=mediapipe.solutions.drawing_utils #dibujo los movimientos
screen_width, screen_height = pyautogui.size() #obtiene el alto y ancho de la pantalla


cam=cv2.VideoCapture(0) #utilizo la primera camara de mi pc
x1=y1=x2=y2=0

is_dragging = False  # Flag para saber si estamos arrastrando

while True:
    _,image = cam.read() #capturo la camara
    image_height, image_width, _ = image.shape
    image=cv2.flip(image,1) #posicion 1 eje vert
    rgb_image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #convertir imagen a rgb
    salida_manos= captura_manos.process(rgb_image)#capturo las manos
    all_hands= salida_manos.multi_hand_landmarks #capturo todas las manos

    #valida si hay manos
    if all_hands:
        #que capture una por una
        for hand in all_hands:
            op_dibujo.draw_landmarks(image,hand)
            una_mano_landmarks=hand.landmark
            for id, lm in enumerate(una_mano_landmarks):
                x=int(lm.x * image_width)
                y=int(lm.y * image_height)

                #print(lm.x,lm.y) #hallar la posicion
                #print (x,y) #altura y ancho de los puntos
                if id == 8: #id del cuarto dedo
                    #captura el mouse en el plano x , y
                    mouse_x= int(screen_width/image_width * x)
                    mouse_y= int(screen_height/image_height * y)
                    pyautogui.moveTo(mouse_x,mouse_y, duration=0.1) #mueve al mouse en la posicion

                    #para capturar un click
                    x1=x
                    y1=y

                    cv2.circle(image,(x,y),15,(0,255,255)) #dibuja circulos en los dedos
                if id == 4: #id del pulgar
                    #para capturar un click
                    x2=x
                    y2=y

                    cv2.circle(image,(x,y),15,(0,255,255))
       # Distancia entre los dedos índice y pulgar (euclidiana)
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        print(dist)
        if(dist < 20):
            pyautogui.click() #captura click del mouse
            print("Click")



    cv2.imshow("captura de video de los movimientos de la mano",image)
    key=cv2.waitKey(1)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()



