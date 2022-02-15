import qrcode

qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)

data = """ Personal Information
    Name: Justin Lawrence DL.Villas
    Age: 18 yrs old
    Address: 117, Sininguelas St. Brgy. Binakas, Lubang, Occidental Mindoro
    Cellphone Number: 09091234567
    Email: justinlawrencedlvillas@gmail.com
 """
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("Personal Data.png")
