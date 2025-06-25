# import matplotlib.pyplot as plt        # 첫번째
# from  matplotlib import pyplot as plt  # 두번째
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
        print('통신 에러 발생했습니다')
    return two


#순서2] 년도, 코드국가코드, E입국 , 순서1에서 기술한 순서1함수 getRequestURL()함수호출
def getNatVisitor(yyyymm, nat_cd, ed_cd ):
    url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    serviceKey = "~~~5TwyxNfqJ6cik8%2Fxa0rl52%2FH823b~~~Aw%3D%3D"
    parameter = '?_type=json&serviceKey=' + serviceKey
    parameter = parameter + '&YM=' + yyyymm
    parameter = parameter + '&NAT_CD=' + nat_cd
    parameter = parameter + '&ED_CD=' + ed_cd 
    myurl = url + parameter
    print(myurl)
    ret_data = getRequestURL(myurl)
    print(json.loads(ret_data))
    return  json.loads(ret_data)


#순서3] for년 for월 순서2함수호출 
result = [ ]
for year in range(2017, 2019):  #년
    for month in range(1,13):   #월
        yyyymm = '{0}{1:0>2}'.format( str(year), str(month))
        json_data =  getNatVisitor(yyyymm, '275', 'E' ) #순서2함수호출
        if ( json_data['response']['header']['resultMsg'] == 'OK' ):
            natKorNm = json_data['response']['body']['items']['item']['natKorNm']
            num = json_data['response']['body']['items']['item']['num']
            print('%s년 %s월 %s %s명' %(str(year), str(month),natKorNm ,num))
            result.append([yyyymm]+[natKorNm]+['275']+[num])


print()
print(result) #['201712', '미  국', '275', 66763]
print()

time.sleep(1)
df = pd.DataFrame(result)
path  = './data/tour0626.csv'
df.to_csv(path, encoding='cp949')
print(path, '파일저장 성공했습니다 ')


ymVisit = [ ]
cnVisit = [ ]
index = []
i = 0 

for item in result:
    ymVisit.append(item[0])
    cnVisit.append(item[3])

plt.figure(figsize=(14,6))
plt.bar(ymVisit,cnVisit)
plt.title('미국 출입국 통계데이터')
plt.xlabel('방한년월')
plt.xlabel('방문카운트')
plt.show()










