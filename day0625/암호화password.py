"""
work시리즈] 문자열에서 암호화   클래스x,함수x
 문자함수 index(), count(), len(), replace(), str()
 문자열 추출 [시작:끝]
 권장변수  domain, index, pw1,pw2,pw3, password 
# strUrl = "http://kakao.com"   kak50!
# strUrl = "http://geegle.com"  goo63!   
# strurl = "http://naver.com"   nav51!
# strurl = "http://estesoft.com"   est72!
해결1] http:// https://  제외시키고, 도메인이름시작 3글자 접두사 가져오기
해결2] 도메인이름 글자수 ,  e글자포함갯수,  마지막!강제성   마지막 !대신 @@덧붙여도 됩니다
문자열 추출 연습해야 판다스에서 행에서 열에서 데이터 추출 이해하기 편합니다
"""
print()
url = "http://estesoft.com"
my_str = url.replace("http://", "")   
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f"비밀번호는 { password} 입니다")
print()


data = ["https://kokao.org", "http://geogle.com", "https://neker.com", "http://mocrosoft.com"] #리스트응용
for i in data :
  domain = i.replace("http://", "").replace("https://", "")
  p1 = domain[:3]
  str_split = domain.split('.')
  p2 = len(str_split[0])
  p3 = domain.count('e')
  password = p1 + str(p2) + str(p3) + '!'
  print(password)


print()