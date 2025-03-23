import qrcode
from PIL import Image

data = input("Enter anything to generate QR: ")

qr = qrcode.make(data)