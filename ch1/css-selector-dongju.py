from bs4 import BeautifulSoup
import urllib.request as request

# 뒤의 인코딩 부분은 "저자:윤동주" 라는 의미입니다.
# 따로 입력할 필요없이 url 부분을 복사해서 사용..

url = "https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"
request = request.urlopen(url)
soup = BeautifulSoup(request, "html.parser")

a_list = soup.select("#mw-content-text > div > ul > li a")

for a in a_list:
    name = a.string
    print ("-", name)