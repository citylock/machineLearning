from bs4 import BeautifulSoup
import urllib.request as request

# HTML 가져오기
url = "https://finance.naver.com/marketindex/"
request = request.urlopen(url)

# HTML 분석하기
soup = BeautifulSoup(request, "html.parser")


# 원하는 데이터 추출하기
price = soup.select_one("div.head_info > span.value").string
print ("usd/krw = ", price)

