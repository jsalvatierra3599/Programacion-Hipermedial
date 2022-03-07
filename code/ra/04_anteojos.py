import cv2

anteojos = cv2.imread('./imagenes/monoculo.jpg')
alto_anteojos, ancho_anteojos, _ = anteojos.shape

talla_anteojos = 1.3
proporciones_anteojos = ancho_anteojos / alto_anteojos
offset_anteojos = 5

area_min = 10000

clasificador = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
clasificador_ojos = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

camara = cv2.VideoCapture(0)
if not camara.isOpened():
    print('No es posible abrir la camara.')
    exit()

ancho_ventana = int( camara.get( cv2.CAP_PROP_FRAME_WIDTH ) )
alto_ventana = int( camara.get( cv2.CAP_PROP_FRAME_HEIGHT ) )

while True:
    ret, frame = camara.read()

    if not ret:
        print('No es posible obtener la imagen')
        break

    frame_byn = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Se detectan las caras
    caras = clasificador.detectMultiScale( frame_byn )

    for (x_cara, y_cara, ancho_cara, alto_cara) in caras:
        if ancho_cara * alto_cara > area_min:
            # se recorta la cara de la imagen original
            cara = frame_byn[ y_cara: y_cara + alto_cara, x_cara: x_cara + ancho_cara ]
            # luego se identifican los ojos dentro de la cara
            ojos = clasificador_ojos.detectMultiScale(cara)

            # si el numero de ojos no es dos, se descarta.
            if len(ojos) != 2:
                continue
            
            # Se obtienen las coordenadas x, y de los ojos.
            (x_ojo0, y_ojo0, ancho_ojo0, _) = ojos[0]
            (x_ojo1, y_ojo1, ancho_ojo1, _) = ojos[1]

            if x_ojo0 > x_ojo1:
                x_ojo = x_ojo0 + int( ancho_ojo0 / offset_anteojos )
                y_ojo = y_ojo0
                ancho_ojo = ancho_ojo0
            else:
                x_ojo = x_ojo1 + int( ancho_ojo1 / offset_anteojos )
                y_ojo = y_ojo1
                ancho_ojo = ancho_ojo1

            ancho_anteojos = int( ancho_ojo * talla_anteojos )
            alto_anteojos = int( ancho_anteojos / proporciones_anteojos )
            anteojos = cv2.resize( anteojos, (ancho_anteojos, alto_anteojos) )
            x_anteojos = x_ojo + x_cara
            y_anteojos = y_ojo + y_cara

            # Se selecciona el ojo derecho
            if x_anteojos >= 0 and y_anteojos >= 0 and \
                x_anteojos+ancho_anteojos <= ancho_ventana and y_anteojos+alto_anteojos <= alto_ventana:
                roi = frame[ y_anteojos: y_anteojos+alto_anteojos, x_anteojos: x_anteojos+ancho_anteojos ]
                roi = cv2.bitwise_and(anteojos, roi)
                frame[ y_anteojos: y_anteojos+alto_anteojos, x_anteojos: x_anteojos+ancho_anteojos ] = roi

    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()