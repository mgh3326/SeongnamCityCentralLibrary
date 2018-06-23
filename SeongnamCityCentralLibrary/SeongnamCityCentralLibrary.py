import urllib.request
from bs4 import BeautifulSoup
import requests
from itertools import count
import os
import datetime


def get_html(url):  # 날씨 코드를 받아오기
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def getLibraryStatus():  # 결과값을 년도, 달별로 받기
    my_url = "http://211.253.111.152:8061/RoomStatus.aspx"
    html = get_html(my_url)  # html로 문자열 반환 자료값을 받기
    soup_data = BeautifulSoup(html, 'html.parser')  # beautiful함수로 실행
    store_table = soup_data.find_all('table')
    # 이렇게 해서 파싱 해야될것 같다. 왜냐하면 클래스가 안 정해져있기 때문이다.
    print(store_table)
    # print(soup_data)
    # f = open("foo.html", 'w', encoding='utf-8')
    # f.write(str(soup_data))
    # f.close()
    return


getLibraryStatus()
