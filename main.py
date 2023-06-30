import os
import requests
import base64
import qrcode
import time

while True:
    try:
        response = requests.get('http://127.0.0.1:5001/api/random')
        random_string = response.text.strip()
        
        base64_encoded = base64.b64encode(random_string.encode()).decode()
        
        qr = qrcode.QRCode()
        qr.add_data(base64_encoded)
        qr.make(fit=True)
        
        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')
        
        time.sleep(3)  # 3초간 대기
    except KeyboardInterrupt:
        break  # Ctrl+C를 누르면 반복 종료
