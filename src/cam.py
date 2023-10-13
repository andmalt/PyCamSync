import cv2
from datetime import datetime

def record_video():
    # Accendi la webcam
    webcam = cv2.VideoCapture(0)

    # Verifica se la webcam è stata aperta correttamente
    if not webcam.isOpened():
        print("Impossibile accedere alla webcam")
        return

    date = datetime.now()
    formatted_data = date.strftime("%Y-%m-%d_%H-%M-%S-%f")
    video_filename  =  f"video_{formatted_data}.avi"
    # print(video_filename)
    
    # Imposta il codec e crea un oggetto VideoWriter per salvare il video
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(video_filename, fourcc, 30.0, (640, 480)) # HD 1280 - 720
    print('ok')
    
    while True:
        # Leggi un frame dalla webcam
        ret, frame = webcam.read()

        if ret:
            # Scrivi il frame nel video
            out.write(frame)

            # Visualizza il frame
            cv2.imshow("Webcam", frame)

        # Interrompi la registrazione se viene premuto il tasto 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Rilascia le risorse
    webcam.release()
    out.release()
    cv2.destroyAllWindows()
    
    
    
"""
25 fps, 640*480  12mb min
webcam logitech c270 HD
"""
