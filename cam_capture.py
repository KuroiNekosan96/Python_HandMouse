import cv2

class Cam_capture:
    def __init__(self, camera_index=0):
        """Inicializa la captura de video."""
        self.cap = cv2.VideoCapture(camera_index)

    def start_capture(self):
        """Inicia la captura de pantalla."""
        try:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                
                frame = cv2.flip(frame, 1)  # Espejo
                cv2.imshow("Pantalla de captura", frame)

                # Salir con la tecla ESC (código ASCII 27)
                if cv2.waitKey(1) == 27:
                    break
        finally:
            self.release()

    def release(self):
        """Libera la cámara y cierra las ventanas."""
        self.cap.release()
        cv2.destroyAllWindows()
