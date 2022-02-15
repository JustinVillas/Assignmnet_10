import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

Buwan = now.strftime("%B %d, %Y")
Oras = now.strftime("%H:%M")


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode("utf-8")

        # This will be the format of the data within our txt file.
        Data = f"Date Scanned \n     Date: {Buwan} \n     Time: {Oras} \n\n{myData}."

        # This will create a txt file entitled "Personal_Info"
        f = open("Personal Info.txt", "w")
        f.write(Data)
        f.close()

    cv2.imshow("Result", img)
    cv2.waitKey(1)
