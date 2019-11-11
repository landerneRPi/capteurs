# Webcam USB

Mise en œuvre Webcam USB avec Raspberry Pi, Python et OpenCV.

## Configuration Raspberry Pi

Installation des applications pour tester la Webcam USB:

```bash
# installation des applications
$ sudo apt install cheese vlc
```

Test de la Webcam USB en utilisant cheese ou VLC.

Installation des bibliothèques nécessaires pour OpenCV (4.1.1) et python 3.5/3.6/3.7/3.8.

```bash
# installation des bibliothèques
$ sudo apt install libjasper-dev libqtgui4 libqt4-test libcblas-dev libatlas-base-dev libhdf5-dev libhdf5-serial-dev
```

## Programmation Python

Création et activation d'un environnement python virtuel:

```bash
$ python3 -m venv webcamusb
$ cd webcamusb
$ source bin/activate
(webcamusb) $ 
```

Installation des dépendances:

```bash
(webcamusb) $ pip3 install -r requirements.txt
Collecting opencv-python==4.1.1.26 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/5e/7e/bd5425f4dacb73367fddc71388a47c1ea570839197c2bcad86478e565186/opencv_python-4.1.1.26-cp36-cp36m-manylinux1_x86_64.whl
Collecting numpy>=1.11.3 (from opencv-python==4.1.1.26->-r requirements.txt (line 1))
  Downloading https://files.pythonhosted.org/packages/d2/ab/43e678759326f728de861edbef34b8e2ad1b1490505f20e0d1f0716c3bf4/numpy-1.17.4-cp36-cp36m-manylinux1_x86_64.whl (20.0MB)
Installing collected packages: numpy, opencv-python
Successfully installed numpy-1.17.4 opencv-python-4.1.1.26
(webcamusb) $
```

Utilisation de la Webcam, capture vidéo et affichage dans une fenêtre graphique de chaque trame par le programme *prog_webcam_capture_video.py*:

```python
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
```

```bash
# démarrer le programme 
(webcamusb) $ python3 prog_webcam_capture_video.py
```

Désactivation de l'environnement python virtuel:

```bash
(webcamusb) $ deactivate
$
```

## Références

  * https://fr.wikipedia.org/wiki/Webcam
  * https://fr.wikipedia.org/wiki/OpenCV
  * https://pypi.org/project/opencv-python/
  * https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
  * https://github.com/opencv/opencv/tree/master/data/haarcascades

