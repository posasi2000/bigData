import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import random  # 임의 추출을 위한 라이브러리

# MobileNet SSD 모델을 
def load_mobilenet_ssd():
    # Caffe 모델 파일 경로 (prototxt와 caffemodel)
    prototxt_path = './test/MobileNetSSD_deploy.prototxt'  # 모델 구조 파일
    model_path = './test/MobileNetSSD_deploy.caffemodel'  # 학습된 모델 파일
    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)  # 모델 불러오기
    return net  # 불러온 모델 반환

# MobileNet SSD로 감지 가능한 객체 목록
class_names = ["background", "aeroplane", "bicycle", "bird", "boat", 
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", 
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep", 
               "sofa", "train", "tvmonitor"]

# 얼굴 감지 모델 로드 (Haar haarcascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 이미지가 저장될 폴더 경로 설정
image_folder = './test1/'  # 사람 포함된 이미지를 저장할 폴더
face_image_folder = './test2/'  # 얼굴이 감지된 이미지를 저장할 폴더

# 오래된 이미지 삭제 함수
def clean_old_images(image_folder, max_images=100):
    """
    이 함수는 이미지 폴더에 저장된 이미지 수가 max_images를 초과할 경우
    가장 오래된 이미지를 삭제하여 이미지 수를 조절합니다.
    
    매개변수:
    image_folder (str): 이미지가 저장된 폴더 경로
    max_images (int): 유지할 최대 이미지 수 (기본값은 100)
    """
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]  # 이미지 파일 목록
    if len(image_files) > max_images:  # 이미지 수가 max_images를 초과하면
        for image_file in image_files[:len(image_files) - max_images]:
            os.remove(os.path.join(image_folder, image_file))  # 오래된 이미지 삭제
        print(f"{len(image_files) - max_images}개의 이미지를 삭제했습니다.")  # 삭제된 이미지 개수 출력

# 동영상에서 이미지를 추출하여 사람 포함 여부 확인 후 저장
video = cv2.VideoCapture('./test/scuba.mp4')  # 동영상 파일 열기
num = 0
image_count = 50  # 최대 50개 이미지만 추출

# MobileNet SSD 모델 불러오기
net = load_mobilenet_ssd()

while video.isOpened() and num < image_count:
    check, frame = video.read()
    if not check:  # 동영상이 끝났다면
        print('동영상 끝났습니다.')
        break

    # cv2.imshow('test', frame)
    (h, w) = frame.shape[:2]  # 프레임의 높이와 너비
    blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)  # 이미지 전처리
    net.setInput(blob)  # 모델 입력 설정
    detections = net.forward()  # 사람 탐지를 위한 전방향 패스 실행

    # 탐지된 객체가 사람인지 확인
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]  # 탐지된 객체의 신뢰도

        if confidence > 0.2:  # 신뢰도가 20% 이상일 경우
            idx = int(detections[0, 0, i, 1])  # 탐지된 객체의 클래스 인덱스
            if class_names[idx] == 'person':  # 사람이 탐지되었을 경우
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])  # 사람의 위치를 계산
                (startX, startY, endX, endY) = box.astype("int")  # 좌표를 정수로 변환

                # 이미지를 파일로 저장
                mypath = f'{image_folder}myscuba_{num}.jpg'
                cv2.imwrite(mypath, frame)  # 이미지 저장
                num += 1  # 이미지 번호 증가
                break  # 한 명만 탐지된 후 루프 종료

    clean_old_images(image_folder, max_images=300)  # 이미지가 너무 많으면 오래된 이미지 삭제
video.release()  # 비디오 캡쳐 객체 해제

# 저장된 이미지 목록 가져오기
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# 사람이 포함된 이미지가 없을 경우 처리
if len(image_files) == 0:
    print("사람이 포함된 이미지가 없습니다.")
else:
    # 사람이 포함된 이미지 중에서 최대 4개까지 임의로 선택
    num_images_to_display = min(4, len(image_files))  # 최대 4개 이미지 선택
    selected_images = random.sample(image_files, num_images_to_display)  # 임의로 4개 선택

    # 2행 2열 형태로 이미지를 출력할 수 있는 subplot 생성
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))  # 2행 2열 그리드로 설정
    axes = axes.flatten()  # axes를 1D 배열로 변환하여 반복문에서 처리

    # 선택된 이미지를 순차적으로 출력
    for i, image_file in enumerate(selected_images):
        image_path = os.path.join(image_folder, image_file)

        image = cv2.imread(image_path)  # 이미지를 읽어옴
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 이미지를 흑백으로 변환
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 얼굴을 탐지

        (h, w) = image.shape[:2]
        # MobileNet SSD를 사용하여 이미지에서 사람 탐지
        blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)
        net.setInput(blob)
        detections = net.forward()

        # 얼굴에 초록색 사각형 그리기
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 사람의 전신에 파란색 사각형 그리기
        for j in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, j, 2]

            if confidence > 0.2:  # 신뢰도가 20% 이상일 경우
                idx = int(detections[0, 0, j, 1])
                if class_names[idx] == 'person':  # 사람이 탐지된 경우
                    box = detections[0, 0, j, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")
                    cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)

                    # 얼굴이 감지된 이미지를 별도의 폴더에 저장
                    face_image_path = os.path.join(face_image_folder, f"face_detected_{image_file}")
                    cv2.imwrite(face_image_path, image)

        # OpenCV는 BGR 형식으로 이미지를 읽기 때문에 RGB로 변환
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # 각 이미지를 axes[i]에 맞춰서 출력
        axes[i].imshow(image_rgb)
        axes[i].axis('off')  # 축 제거
        axes[i].set_title(f'Image {i + 1}')  # 제목 설정

    plt.tight_layout()  # 레이아웃 조정
    plt.show()  # 이미지를 화면에 출력
    print('이미지 추출 성공 했습니다 AI국방부 1:20')



print()
