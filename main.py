import cv2

def leer_QR(ruta_qr):
    img = cv2.imread(ruta_qr)
    detector = cv2.QRCodeDetector()
    data = detector.detectAndDecode(img)
    return data[0]

print(leer_QR("img.png"))