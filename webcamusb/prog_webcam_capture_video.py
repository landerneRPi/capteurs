import cv2

# configuration capture vidéo premier périphérique
capvideo = cv2.VideoCapture(0)

while(True):
    # capture trame par trame
    ret, frame = capvideo.read()

    # affichage de la trame dans une fenêtre graphique
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# fin de la boucle
# arrêt de la capture vidéo et libération des ressources
capvideo.release()
cv2.destroyAllWindows()
