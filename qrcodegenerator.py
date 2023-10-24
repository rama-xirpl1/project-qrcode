import qrcode
import image
qr = qrcode.QRCode(
    version = 15, #versi qrcode
    box_size = 10, #untuk ukuran qrcode
    border = 5 #ukuran putih-putihnya qrcode
)

data = "https://youtu.be/IKKar5SS29E?si=49mJuXShvtMyntKA"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_color = "white") #setiing warna qrcode
img.save("link.png") 