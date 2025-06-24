# pip install  numpy  pandas  matplotlib  seaborn  scikit-learn  nltk  # 한번에 다 설치
# pip install opencv-python
# pip list

# ModuleNotFoundError: No module named 'Crypto'
# pip install pycryptodome 

from Crypto.Cipher import PKCS1_OAEP  #공개키값 생성에 필요함
from Crypto.PublicKey import RSA      #공개키값 생성에 필요함
import time
"""
공개 암호화 알고리즘으로는 RSA, ECC, 전자서명 등이 존재하면 RSA방식은 2개키가 필요함 
RSA = 리베스트-샤미르-애들먼(Rivest-Shamir-Adleman)암호는 공개 키 암호 방식의 하나로, 암호화뿐만 아니라 전자서명이 가능한 최초의 알고리즘으로 알려져 있다.
RSA가 갖는 전자서명 기능은 인증을 요구하는 전자 상거래 등에 RSA의 광범위한 활용을 가능하게 하였다.
https://ko.wikipedia.org/wiki/RSA_암호
"""

# key 생성 및 저장
def make_key():
    pr_key = RSA.generate(2048) # 2048길이의 키 생성
    print(pr_key)
    pu_key = pr_key.public_key()
    print(pu_key)

    pr_file = open('./data2/pr.key','wb')
    pr_file.write(pr_key.export_key('PEM'))
    pr_file.close()

    pu_file = open('./data2/pu.key', 'wb')
    pu_file.write(pu_key.export_key('PEM'))
    pu_file.close()

    print('pu.key, pr.key 파일이 생성되었습니다 ')
    print('- ' * 60)


make_key() # 순서1] 첫번째 함수  키값생성 파일생성


# from Crypto.Cipher import PKCS1_OAEP 
# 순서2] 메시지 암호화
def encrypt_msg(msg, key):
    tool = PKCS1_OAEP.new(key)
    msg_enc = tool.encrypt(msg)
    return msg_enc


# 순서3] 메시지 복호화
def decrypt_msg(msg, key):
    tool = PKCS1_OAEP.new(key)
    msg_dec = tool.decrypt(msg)
    return msg_dec


# 순서4]  파일에서 키 가져오기
def get_key(path):
    fr = open(path, 'rb')
    key = RSA.importKey(fr.read())
    return key


#  순서5] 메인 함수
def main():
    msg = 'do you know python language 파  &$@  이 썬' # 최대 86자까지 암호화 가능, 암호화 하면  128비트로 변환
    pu_key = get_key('./data2/pu.key')
    msg_enc = encrypt_msg(msg.encode(), pu_key)

    print("원 문 :", msg)
    print()
    time.sleep(1)
    print("암호화 :", msg_enc)
    print()

    pr_key = get_key('./data2/pr.key') # 프라이빗 키를 가져옴
    msg_dec = decrypt_msg(msg_enc, pr_key) #  복호화
  
    time.sleep(1)
    print("복호화 ", msg_dec.decode('utf-8'))  #한글은 복호화 decode안하면 한글 깨짐 

main() # 두번째  main함수 호출
print()