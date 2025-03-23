from wifi_qrcode_generator import wifi_qrcode

qr_code = wifi_qrcode('POCO M3', hidden=False, authentication_type="WPA", password="12345678")
qr_code_img = qr_code.make_image()
qr_code_img.save("qr.png")