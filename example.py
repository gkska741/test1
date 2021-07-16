"""

import requests
from bs4 import BeautifulSoup

1.
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073861 에서 활용 신청 
2.
로컬에서 진행 시 패키지 설치
pip install beautifulsoup4 requests lxml


KEY = 'iTpdD5hhMW71PQus57ztCitlpMM8T4ntl3mEe%2FTzhseoUcgTpG5kR29kq7%2FcxYy4ky3ufUl%2B5wvT5JURzmFmTg%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'
# print(url)
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

#코드 추가

if dust > 150:
    print("미세먼지 농도가 매우 높습니다! 주의하세요!")
elif dust > 80:
    print("미세먼지 농도가 약간 높습니다! 주의하세요")
elif dust > 30:
    print("미세먼지 농도가 적당한 수준입니다.")
else:
    print("미세먼지가 거의 없습니다. 공기가 깨끗합니다!")
"""



import random

lotto = []
i = 0
a = 0
while i != 6:
    a = 0
    while a == 0:
        x = random.choice(range(1, 46))
        if x in lotto:
            pass
        else:
            lotto.append(x)
            a = 1
    i += 1

print(lotto)
