import qrcode


def start():
    data = input("Enter the text or URL: ")
    filename = input("Enter the filename: ")

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    image = qr.make_image(fill_color="black", black_color="white")
    image.save(filename)
    print(f"QR code saved as {filename}")
