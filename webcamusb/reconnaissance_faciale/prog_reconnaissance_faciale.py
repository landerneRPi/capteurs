import cv2
import sys

# telecharger https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# comme argument au programme
cascPath = sys.argv[1]
# charger et configurer la méthode de classification (face, yeux...)
faceCascade = cv2.CascadeClassifier(cascPath)

# configuration capture vidéo premier périphérique
video_capture = cv2.VideoCapture(0)

while True:
    # capture trame par trame
    ret, frame = video_capture.read()

    # conversion en niveau de gris pour traitement
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # traitement
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # dessine un rectangle vert autour des éléments trouvés (face, yeux...)
    # sur la trame originale
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # affiche la trame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# fin de la boucle
# arrêt de la capture vidéo et libération des ressources
video_capture.release()
cv2.destroyAllWindows()

