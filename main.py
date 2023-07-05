import requests
import base64
import qrcode
import time

while True:
    try:
        response = requests.get('http://127.0.0.1:8080/api/random')
        random_string = response.json()

        print(random_string)

        if 'generateNum' not in random_string:
            print('server error')
            continue

        random_string = random_string['generateNum']

        base64_encoded = base64.b64encode(random_string.encode()).decode()

        qr = qrcode.QRCode()
        qr.add_data(base64_encoded)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode.png')

        time.sleep(1)
    except KeyboardInterrupt:
        break  # Ctrl+C를 누르면 반복 종료
