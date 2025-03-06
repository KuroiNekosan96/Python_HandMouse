import cv2
import mediapipe as mp

mpManos= mp.solutions.hands
manos=mpManos.Hands(
    static_image_mode=False, #asume que esta video en directo y no es una imagen estatica a analizar
    model_complexity=1, #modelo complejo para obtener un buen modelo
    #niveles de confianza al 70% deteccion y seguimiento
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1 #numero maximo de manos que puede detectar

)
def main():
    cap=cv2.VideoCapture(0) #utiliza la primera camara que encuentra
    draw=mp.solutions.drawing_utils #utiliza para dibujar lo que va detectar

    try:
        while cap.isOpened():
            ret,frame = cap.read() #lee el video por frame
            #si no retorna un frame, sale del bucle
            if not ret:
                break
            frame = cv2.flip(frame,1) #para girar la imagen como un espejo
            
            frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #Dar color a lo que detecta
            
            processed=manos.process(frameRGB)
            landmarks_list = [] #recibe todos los puntos de referencia

            #si encuentra manos, dibujará marcadores
            if processed.multi_hand_landmarks:
                mano_landmark=processed.multi_hand_landmarks[0]
                draw.draw_landmarks(frame,mano_landmark,mpManos.HAND_CONNECTIONS)
                
                #recorre para capturar las posiciones de la mano
                for lm in mano_landmark.landmark:
                    landmarks_list.append((lm.x, lm.y)) #posiciones en x e y
                print(landmarks_list) #imprime las posiciones 21en total




            cv2.imshow("Pantalla de captura",frame) #muestra la pantalla o el frame
            #para salir de la pantalla
            key=cv2.waitKey(1)
            if key == 27:
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


