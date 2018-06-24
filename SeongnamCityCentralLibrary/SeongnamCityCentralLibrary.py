import urllib.request
from bs4 import BeautifulSoup
import requests
from itertools import count
import os
import datetime


class SeatStatus:
    readingRoomName = ""  # 열람실명
    entireSeat = 0  # 전체좌석
    serviceSeat = 0  # 사용좌석
    remainingSeat = 0  # 잔여좌석
    Utilization = 0  # 이용률(%)
    waitingCount = 0  # 대기자수
    callNumber = 0  # 호출번호
    scheduledNumber = 0  # 예정번호


def get_html(url):  # 날씨 코드를 받아오기
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def GetLibraryStatus():  # 결과값을 년도, 달별로 받기
    # Body	__VIEWSTATE	%2FwEPDwUKMTgwNzQzMjM3MWRkrP3scz%2FitEFfjlxuP%2BZ2QbQBxpQ%3D
    # Body	__VIEWSTATEGENERATOR	880FA830
    # Body	__EVENTVALIDATION % 2FwEWAgKWuaeTBgLJ0ILXB9jZM5AHjC1xDQUzHOiGSoAW2k93
    # Body	Roon_no	4
    # http://211.253.111.152:8061/RoomStatus.aspx?__VIEWSTATE=%2FwEPDwUKMTgwNzQzMjM3MWRkrP3scz%2FitEFfjlxuP%2BZ2QbQBxpQ%3D&__VIEWSTATEGENERATOR=880FA830&__EVENTVALIDATION=%2FwEWAgKWuaeTBgLJ0ILXB9jZM5AHjC1xDQUzHOiGSoAW2k93&Roon_no=4
    # 파라미터 정리
    # baes64인가 하나도 모르겠네
    my_url = "http://211.253.111.152:8061/RoomStatus.aspx?__VIEWSTATE=%2FwEPDwUKMTgwNzQzMjM3MWRkrP3scz%2FitEFfjlxuP" \
             "%2BZ2QbQBxpQ%3D&__VIEWSTATEGENERATOR=880FA830&__EVENTVALIDATION" \
             "=%2FwEWAgKWuaeTBgLJ0ILXB9jZM5AHjC1xDQUzHOiGSoAW2k93&Roon_no=1 "
    # 뒤에 숫자 바꾸면 열람실 선택할수 있음
    html = get_html(my_url)  # html로 문자열 반환 자료값을 받기
    soup_data = BeautifulSoup(html, 'html.parser')  # beautiful함수로 실행
    store_table = soup_data.find_all('table')
    # 이렇게 해서 파싱 해야될것 같다.  왜냐하면 클래스가 안 정해져있기 때문이다.
    table_title = store_table[1].findAll('td', attrs={'class': 'table_title'})

    len(table_title)


    for i in range(int(len(store_table[1].findAll('td')) / len(table_title)) + 1):
        seatStatusList.append(SeatStatus())

    for idx, val in enumerate(store_table[1].findAll('td')):
        if idx % len(table_title) == 0:
            seatStatusList[int(idx / len(table_title))].readingRoomName = val.text.strip()
        elif idx % len(table_title) == 1:
            seatStatusList[int(idx / len(table_title))].entireSeat = val.text.strip()
        elif idx % len(table_title) == 2:
            seatStatusList[int(idx / len(table_title))].serviceSeat = val.text.strip()
        elif idx % len(table_title) == 3:
            seatStatusList[int(idx / len(table_title))].remainingSeat = val.text.strip()
        elif idx % len(table_title) == 4:
            seatStatusList[int(idx / len(table_title))].Utilization = val.text.strip()
        elif idx % len(table_title) == 5:
            seatStatusList[int(idx / len(table_title))].waitingCount = val.text.strip()
        elif idx % len(table_title) == 6:
            seatStatusList[int(idx / len(table_title))].callNumber = val.text.strip()
        elif idx % len(table_title) == 7:
            seatStatusList[int(idx / len(table_title))].scheduledNumber = val.text.strip()
        print(idx, val)
        # print(soup_data)
        # f = open("foo.html", 'w', encoding='utf-8')
        # f.write(str(soup_data))
        # f.close()
    return

seatStatusList = []
GetLibraryStatus()
print("Finish")
