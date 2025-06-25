from selenium import webdriver
import time


CoffeeBean_URL = "https://www.coffeebeankorea.com/store/store.asp"
driver = webdriver.Chrome() 
        
driver.get(CoffeeBean_URL)
time.sleep(20)  #웹페이지 연결할 동안 20초 대기

driver.close()
print('초간단 웹크롤링 testing')


"""
Created TensorFlow Lite XNNPACK delegate for CPU.
CPU에 의존하는 대신 일부 기기에 존재하고 있는 GPU또는 DSP와 같은 하드웨어 가속기에 돌리도록 "위임"하여 성능과 에너지 효율성을 높일 수 있게 하는 것이 delegate입니다.
Tensorflow Lite에서는 4가지 delegate를 제공하고 있는데요, iOS, 구형 안드로이드, 신형안드로이드 등등 delegate가 있지만 제가 가장 자주 많이 사용하는 것은 GPU Delegate입니다!
"""
