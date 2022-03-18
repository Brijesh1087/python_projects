import qrcode
print("	QRCode Generator ")
url = input('Enter Text To QRCode : ')
qr = qrcode.make('https://cyber108705.github.io/Corlia/')
qr.save("qrcode.png")