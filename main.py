import os
import requests
import base64
import qrcode

# API에서 랜덤 문자열 가져오기
response = requests.get('http://127.0.0.1:5001/api/random')  # 
random_string = response.text.strip()

# 문자열을 base64로 인코딩
base64_encoded = base64.b64encode(random_string.encode()).decode()

# QR 코드 이미지 생성
qr = qrcode.QRCode()
qr.add_data(base64_encoded)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')  # QR 코드 이미지를 저장할 경로와 파일 이름을 지정합니다.
