from bs4 import BeautifulSoup
import urllib.request as request

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# urlopen() 으로 데이터 가져오기
res = request.urlopen(url)

# BeautifulSoup 으로 분석하기
soup = BeautifulSoup(res, 'html.parser')

# 데이터가 제대로 들어있는지 확인
print(soup.prettify())

# 원하는 데이터 추출하기
title = soup.find("title").string
wf = soup.find('wf').string
print (title)
print (wf)

