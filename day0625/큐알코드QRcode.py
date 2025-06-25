

# pip install  numpy  pandas  matplotlib  seaborn  scikit-learn  nltk  # 한번에 다 설치
# pip install opencv-python
# pip list

# OpenCV = Open Source Computer Vision 라이브러리 
# pip install opencv-python 설치

# pip install captcha
# from captcha.image import ImageCaptcha

# pip install faker
# from faker import Faker

# pip install qrcode
import qrcode
url = 'https://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./data2/QR_code.png')
print('./data2/QR_code.png 저장 성공했습니다')

import cv2
image = cv2.imread('./data2/QR_code.png')
cv2.imshow("title", image)
cv2.waitKey(0)
cv2.destroyAllWindows()




