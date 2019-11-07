from bs4 import BeautifulSoup

html = """"
<html><body> 
    <ul>
        <li><a href="http://www.naver.com">Naver</a></li>
        <li><a href="http://www.daum.net">Daum</a></li>
    </ul>
</body></html>
"""

# HTML 분석하기
soup = BeautifulSoup(html, 'html.parser')

# extract multiple elements using find_all()
links = soup.find_all("a")

# link 목록 추출하기
for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, " > ", href)