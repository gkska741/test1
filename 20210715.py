
# <웹에서 환율정보 수집하기>
import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
response = requests.get(url)

data = BeautifulSoup(response.text, 'html.parser')

#print(response.status_code)
#print(data.select_one('#exchangeList > li.on > a.head.usd > div > span.value'))

#---------------------------------------------------------------------------------#
# <API활용하기> -> 나이예측프로그램
# 특정 프로그램을 vs코드에서 사용할수 있도록 배포한 것 -> 리퀘스트 모듈 이용.
import requests
from bs4 import BeautifulSoup
name = input("이름은?")
url = f'https://api.agify.io/?name={name}'

response = requests.get(url).json()
name = response['name']
age = response['age']

string = f'{name}의 나이는 {age}살입니다.'

print(string)
print(string)
print(string)

print("https://www.metaweather.com/api/")
"뭔가 달라짐"