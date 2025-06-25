# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
import urllib.parse
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import rc

# 음수표기 관리
import matplotlib as mpl
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus']=False

font_name = font_manager.FontProperties(fname='c:/windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

import pandas as pd
import time
#--------------------------------------------------------------------------------------------
import urllib.request  
import json


#순서1] url주소 접속성공 확인 
def getRequestURL(myurl, enc='utf-8'):
    request  = urllib.request.Request(myurl)
    response = urllib.request.urlopen(request)
    if response.getcode() == 200 :
        first = response.read()
        two = first.decode(enc)
    else:
        print('AirKorea 통신 에러 발생했습니다')
    return two


#순서2] 
def getAirSido( returnType, rownum , pageNo, sidoName , ver):
    url='http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
    serviceKey = "~~~5TwyxNfqJ6cik8%2Fxa0rl52%2FH823b~~~Aw%3D%3D"

    parameter = '?serviceKey=' + serviceKey
    parameter =  parameter + '&returnType=' + returnType
    parameter =  parameter + '&numOfRows=' + rownum 
    parameter =  parameter + '&pageNo=' + pageNo
    parameter =  parameter + '&sidoName=' + urllib.parse.quote(sidoName) +'&ver=' + ver
    myurl = url + parameter
    print(myurl)
    ret_data = getRequestURL(myurl)
    print(json.loads(ret_data))
    return  json.loads(ret_data)


#순서3] for6회 
result = [ ]
for i in range(6):  
    json_data =  getAirSido('json', '100', '1', '서울', '1.0' ) #순서2함수호출
    if (json_data['response']['header']['resultMsg'] == 'NORMAL_CODE' ):
        sidoName = json_data['response']['body']['items'][i]['sidoName']
        stationName = json_data['response']['body']['items'][i]['sidoName']
        o3Value = json_data['response']['body']['items'][i]['o3Value']
        no2Value = json_data['response']['body']['items'][i]['no2Value']
        pm10Grade = json_data['response']['body']['items'][i]['pm10Grade']
        print(f'sidoName={sidoName} stationName={stationName} o3Value={o3Value} no2Value={no2Value} pm10Grade={pm10Grade}')
        result.append([sidoName]+[stationName]+[o3Value]+[no2Value]+[pm10Grade])


print()
print(result) 
print()

time.sleep(1)
df = pd.DataFrame(result)
path  = './data/air0626.csv'
df.to_csv(path, encoding='cp949')
print(path, '파일저장 성공했습니다 ')










