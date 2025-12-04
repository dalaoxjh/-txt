import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"}

def getPositionInfo(detail_url):
    res = requests.get(detail_url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    job = soup.find(class_="new_job_name").find(name='span').string
    companyName = soup.find(class_="com-name").string.strip()
    position = soup.find(class_="job_position").string
    month = soup.find(class_="job_time cutom_font").string
    price=soup.find(class_='job_money cutom_font').string
    month = month.encode()
    month = month.replace(b"\xee\x8b\xbf", b"0").replace(b"\xee\xa2\x9c", b"1").replace(b"\xee\x90\xb7",b"2")
    month = month.replace(b"\xee\x81\xa5",b"3").replace(b"\xee\xad\xb1", b"4").replace(b"\xee\xb2\xae", b"5")
    month = month.replace(b"\xef\x8a\x98", b"6").replace(b"\xef\x80\xa6",b"7").replace(b"\xee\xa1\xb1", b"8").replace(b"\xee\xbe\xad", b"9")
    month = month.decode()
    print(f"{job},{companyName},{position},{month},{price}")
    with open("工作数据.txt", "a",encoding='utf-8') as f:
                f.write(f'{job},{companyName},{position},{month},{price}'+'\n')
for i in range(1, 6):

    url = f"https://www.shixiseng.com/interns?page={i}&type=intern&keyword=python%E5%BC%80%E5%8F%91&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend="
    res = requests.get(url, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all(class_="title ellipsis font")

    for item in titles:
        detail_url = item.attrs["href"]
        getPositionInfo(detail_url)

    # 使用time.sleep()停顿1秒
    time.sleep(1)
