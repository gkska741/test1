# review

menus = ['치킨', '햄버거', '피자']
"""
for menu in menus:
    print(menu) # 단순 반복출력

for menu in menus:
    print(menu, end=' ') #end를 쓰면 줄바꿈 대신 ''안의 내용으로 출력한다

#menus[1] = '족발' # 햄버거 -> 족발 변경

for menu in menus:
    if menu == '햄버거':
        menu = '족발'
    print(menu, end = ' ') # 일시적인 변환

for i in [0, 1, 2]:
    if menus[i] == '햄버거':
        menus[i] = '족발'
    print(menus[i], end = ' ') # menus List의 영구적인 변환
print(menus)

# 이틀 뒤 날씨 출력해보기

import requests
from bs4 import BeautifulSoup
url = 'https://www.metaweather.com/api/location/1132599/'
response = requests.get(url).json()

tomorrow_weather = response.get('consolidated_weather')[2].get('weather_state_name')

print(f'서울의 모레 날씨는 {tomorrow_weather}로 예상됩니다.')
"""


#https://api.telegram.org/bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow
#https://api.telegram.org/bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow/getme
#https://api.telegram.org/bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow/getUpdates 
#https://api.telegram.org/bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow/sendMessage?chat_id=1835981729&text=반갑습니다
import pprint
from requests import get
import requests

token = 'bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow'
url = f'https://api.telegram.org/{token}/'

data = get(url + 'getUpdates').json()
chat_id = data.get('result')[0].get('message').get('chat').get('id')
text = '뭐하세요?'


sendMessage = f'sendMessage?chat_id={chat_id}&text={text}'
data = requests.get(url + sendMessage)

#---------------------------------------------------------------------------

miseurl = 'http://apis.data.go.kr/6410000/GOA/GOA002?ServiceKey=rW12wD0%2FulJwg6Yyz5cPhEwZeH6c3IMethTgqgF2sjUM7u71uMK1FLa4CZqwGXQgiVtZ06ETrL2JOfCKgEttxg%3D%3D&busno=23054&type=json&numOfRow=10&pageNo=1'
misedata = requests.get(miseurl).json()
dust = misedata.get('result').get('data').get('pm2.5')
print(f"현재 남양주시의 미세먼지 농도는{dust}입니다")



token = 'bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow'
pythonanywhere = 'Kimseonghyun.pythonanywhere.com'
url = f'https://api.telegram.org/{token}/setWebhook?url={pythonanywhere}/telegram'

print(requests.get(url))



from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask!'

token = 'bot1600537681:AAF5pK_YBkyQ8FLsxPu5GKgaaYO9umdnBow'
url = f'https://api.telegram.org/bot{token}/'


@app.route('/telegram', methods=['POST'])
def receive_telegram():
    # 텔레그램으로부터 수신한 요청(request)    
    response = request.get_json()

    if response.get('message') != None:
        chat_id = response.get('message').get('from').get('id')
        text = response.get('message').get('text')

        if text == '광주2반':
            answer = '광주2반 화이팅!!\n ㅎㅎㅎㅎㅎㅎㅎ'
        else:
            answer = '머선 소리고?'

        requests.get(url + f'sendMessage?chat_id={chat_id}&text={answer}')

    return '', 200